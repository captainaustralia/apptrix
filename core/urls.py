from django.urls import path, include
from core.views import ParticipantCreateAPIView, liked_user, ParticipantListAPIView

# ENDPOINTS
# api/clients/create (register endpoint)
# api/auth/login(logout)  ( login/logout endpoints)
# api/clients/user_id/match ( like endpoint)

urlpatterns = [
    path('clients/create/', ParticipantCreateAPIView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('clients/<int:id>/match', liked_user, name='like'),
    path('list/', ParticipantListAPIView.as_view(), name='list')

]
