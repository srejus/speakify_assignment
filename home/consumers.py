import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Get the URL parameters from self.scope
        self.room_group_name = self.scope['path_remaining']
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        
        self.accept()
        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'You are now connected!'
        # }))
        
    def receive(self,text_data):
       text_data_json = json.loads(text_data)
       message = text_data_json.get('message','')
       
       async_to_sync(self.channel_layer.group_send)(
           self.room_group_name,
           {
               'type':'chat_message',
               'message':message,
               'username':text_data_json.get('username','No-Name')
           }
       )
       
  

    def chat_message(self,event):
        message = event['message']
        user = event['username']
        
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username':user
        }))