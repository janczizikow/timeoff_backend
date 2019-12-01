from rest_framework import serializers
from .models import User


class ResetPasswordSerializer(serializers.Serializer):
    reset_token = serializers.CharField(max_length=200)
    password = serializers.CharField(min_length=8,)
    confirm_password = serializers.CharField(min_length=8,)

    def update(self, instance, validated_data):
        new_password = validated_data.pop('password', None)
        instance.set_password(new_password)
        instance.reset_token = ''
        instance.reset_token_expiry = None
        instance.save()
        return instance

    def validate(self, data):
        """
        Check that passwords match
        """
        if data["password"] and data["confirm_password"] and data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("passwords don't match")
        return data
