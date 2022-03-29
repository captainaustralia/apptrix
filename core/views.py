from rest_framework import generics, permissions

from core.api.serializers import ParticipantSerializer
from core.models import Participant


class ParticipantCreateAPIView(generics.CreateAPIView):
    model = Participant
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.AllowAny,)
