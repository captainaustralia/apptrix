from django.contrib import admin

from core.models import Participant

admin.site.register(Participant,admin.ModelAdmin)