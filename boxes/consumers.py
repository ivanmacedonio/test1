# boxes/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from .models import Box

class BoxConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'box_updates'

        # Join room group
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        box_id = data['id']
        titulo = data['titulo']
        color = data['color']

        # Update the box instance in the database
        box = Box.objects.get(pk=box_id)
        box.titulo = titulo
        box.color = color
        box.save()

        # Broadcast the updated data to all connected clients
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'box_update',
                'id': box_id,
                'titulo': titulo,
                'color': color
            }
        )

    def box_update(self, event):
        # Send updated box data to the websocket
        self.send(text_data=json.dumps(event))
