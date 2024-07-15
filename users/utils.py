# utils.py
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model

def get_session_data(session_key):
    User = get_user_model()
    try:
        session = Session.objects.get(session_key=session_key)
        data = session.get_decoded()
        user_id = data.get('_auth_user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            return f"User: {user.username}, Email: {user.email}"
        else:
            return "Anonymous User"
    except Session.DoesNotExist:
        return "Session not found"
