from .message_body import MessageBody
import uuid

class Message():
    def __init__(self, sender_id : str, receiver_id : str, body : MessageBody):
        self.message_id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.body = body

    def get_receiver_id(self) -> str:
        return self.receiver_id

    def get_sender_id(self) -> str:
        return self.sender_id

    def __str__(self):
        return f'[{self.sender_id} -> {self.receiver_id}] {str(self.body)}'
