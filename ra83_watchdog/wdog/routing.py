# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/watchdog/', consumers.WatchdogConsumer.as_asgi()),
]
