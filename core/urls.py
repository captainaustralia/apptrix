from django.urls import path

from core.views import ParticipantCreateAPIView

urlpatterns = [
    path('clients/create/', ParticipantCreateAPIView.as_view()),
]
