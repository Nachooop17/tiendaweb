# admin.py
from django.contrib import admin
from django.contrib.sessions.models import Session
from .utils import get_session_data

class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'expire_date', 'user_info']

    def user_info(self, obj):
        return get_session_data(obj.session_key)
    user_info.short_description = 'User Info'

admin.site.register(Session, SessionAdmin)
