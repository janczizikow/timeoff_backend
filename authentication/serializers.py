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


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    gender = serializers.ChoiceField(choices=User.GENDER, allow_blank=True)
    first_name = serializers.CharField(max_length=255, allow_blank=True)
    last_name = serializers.CharField(max_length=255, allow_blank=True)
    preferred_name = serializers.CharField(max_length=255, allow_blank=True)
    birth_date = serializers.DateField(allow_null=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.preferred_name = validated_data.get('preferred_name', instance.preferred_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance
