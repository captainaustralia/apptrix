from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from APPTRIX import settings
from core.views import mainpage

# ENDPOINTS
# api/clients/create (register endpoint)
# api/auth/login(logout)  ( login/logout endpoints)
# api/clients/user_id/match ( like endpoint)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', mainpage, name='main')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
