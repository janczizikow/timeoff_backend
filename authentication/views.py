from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from timeoff.tasks import send_mail_async
from .models import User
from .serializers import ResetPasswordSerializer


@api_view(['POST'])
def forgot_password(request):
    """
    Sets `reset_token` and `reset_token_expiry` on User
    """
    try:
        user = User.objects.get(email=request.data["email"])
    except User.DoesNotExist:
        raise NotFound("The user does not exist.")
    except KeyError:
        return Response({"detail": "email is missing"}, status=status.HTTP_400_BAD_REQUEST)

    user.reset_token = get_random_string(length=32)
    user.reset_token_expiry = datetime.now(
        tz=timezone.utc) + timedelta(hours=2)
    user.save()
    reset_password_url = settings.CLIENT_URL + \
        'reset-password/?token=' + user.reset_token

    send_mail_async.delay(
        'Timeoff Password Reset',
        render_to_string("emails/reset-password.txt",
                         {"url": reset_password_url}),
        None,
        [user.email],
        html_message=render_to_string("emails/reset-password.html",
                                      {
                                          "client_url": settings.CLIENT_URL,
                                          "url": reset_password_url
                                      }),
        fail_silently=False,
    )

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def reset_password(request):
    """
    Changes password and resets `reset_token` and `reset_token_expiry`
    """
    try:
        user = User.objects.get(
            reset_token=request.data["reset_token"],
            reset_token_expiry__gte=datetime.now(
                tz=timezone.utc) - timedelta(hours=2),
        )
    except User.DoesNotExist:
        raise NotFound("Reset token is invalid or expired.")
    except KeyError:
        return Response({"detail": "reset_token is missing"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ResetPasswordSerializer(instance=user, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(status=status.HTTP_204_NO_CONTENT)
