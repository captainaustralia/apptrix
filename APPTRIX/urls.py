from django.contrib import admin
from django.urls import path, include

# ENDPOINTS
# api/clients/create (register endpoint)
# api/auth/login(logout)  ( login/logout endpoints)
# api/clients/user_id/match ( like endpoint)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
