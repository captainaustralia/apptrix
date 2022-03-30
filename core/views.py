import django_filters
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.api.serializers import ParticipantRegisterSerializer, ParticipantListSerializer
from core.models import Participant, Membership
from core.funcs import send_messages, get_distance_between_users


class ParticipantCreateAPIView(generics.CreateAPIView):
    model = Participant
    serializer_class = ParticipantRegisterSerializer
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


class ParticipantListAPIView(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantListSerializer
    filter_backends = (django_filters.rest_framework.backends.DjangoFilterBackend,)
    filterset_fields = ['name', 'last_name', 'gender']

    def get_queryset(self):
        if self.request.query_params.get('distance'):
            distance = self.request.query_params.get('distance')
            point_user = Participant.objects.get(id=self.request.user.id)
            p_long, p_lat = point_user.longitude, point_user.latitude
            user_in_area = []
            for user in self.queryset.all():
                user_long, user_lat = user.longitude, user.latitude
                if get_distance_between_users(p_long, p_lat, user_long, user_lat) < float(distance):
                    user_in_area.append(user.id)
            user_in_area.remove(self.request.user.id)  # delete auth user id
            in_area = Participant.objects.filter(id__in=user_in_area)
            return in_area
        else:
            return self.queryset


@login_required
def mainpage(request):
    user = Participant.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, 'mainpage.html', context)
