import json
from channels.generic.websocket import AsyncWebsocketConsumer

class chatConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Aquí es donde recibirías el audio, lo transcribirías a texto,
        # lo traducirías y luego enviarías el texto traducido de vuelta.
        # Este es solo un ejemplo simplificado.
        text_data_json = json.loads(text_data)
        coordenadas = text_data_json['coordenadas']
        print('coordenadas------->', coordenadas)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'coordenadas': coordenadas
            }
        )

    async def chat_message(self, event):
        coordenadas = event['coordenadas']
        await self.send(text_data=json.dumps({
            'coordenadas': coordenadas
        }))