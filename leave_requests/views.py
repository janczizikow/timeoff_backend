from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LeaveRequestSerializer
from .models import LeaveRequest


class LeaveRequestList(APIView):
    """
    List all leave requests, or create a new leave request
    """

    def get(self, request, format=None):
        leave_requests = LeaveRequest.objects.filter(user=request.user)
        serializer = LeaveRequestSerializer(leave_requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeaveRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(serializer.data)


class LeaveRequestDetail(APIView):
    """
    Retrieve, update or delete a leave request instance.
    """

    def get_object(self, pk):
        try:
            return LeaveRequest.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        leave_request = self.get_object(pk)
        serializer = LeaveRequestSerializer(leave_request)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        leave_request = self.get_object(pk)
        serializer = LeaveRequestSerializer(leave_request, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        leave_request = self.get_object(pk)
        leave_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
