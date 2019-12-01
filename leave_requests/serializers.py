from rest_framework import serializers

from .models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        exclude = ('user',)

    def validate(self, data):
        if data['end'] < data['start']:
            raise serializers.ValidationError(
                'end date cannot be before the start date')
        return data
