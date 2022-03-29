import django.dispatch
from rest_framework import serializers
from core.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Participant.objects.create_user(**validated_data)
        return user

    class Meta:
        model = Participant
        fields = ('email', 'password', 'name', 'last_name', 'gender', 'avatar')
