# boxes/routing.py
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from boxes import consumers

websocket_urlpatterns = [
    path('ws/boxes/', consumers.BoxConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})