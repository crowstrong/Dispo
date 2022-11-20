from django.urls import re_path

from core import support

websocket_urlpatterns = [
    re_path(r"ws/core/(?P<room_name>\w+)/$", support.SupportRoom.as_asgi()),
]
