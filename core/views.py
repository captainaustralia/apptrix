from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.api.serializers import ParticipantSerializer
from core.models import Participant, Membership
from core.funcs import send_messages


class ParticipantCreateAPIView(generics.CreateAPIView):
    model = Participant
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
def liked_user(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            who_liked = Participant.objects.get(id=request.user.id)
            whose_liked = Participant.objects.filter(id=id)
            if whose_liked.count() == 0:
                return Response(f"Models with id - {id} not found")
            else:
                relation = Membership(who_liked=who_liked, who_was_liked=whose_liked[0])
                relation.save()
                check_relation = Membership.objects.filter(who_liked=whose_liked[0], who_was_liked=who_liked)
                if check_relation.count() != 0:
                    send_messages(who_liked, whose_liked[0])
                    return Response(f'Вы понравились друг другу! Свяжитесь с клиентом {whose_liked[0].email}')
                else:
                    return Response("Liked")
    else:
        return Response(status=401)
