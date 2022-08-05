from .message_body import MessageBody
import uuid

class Message():
    def __init__(self, sender_id : str, receiver_id : str, body : MessageBody):
        self.message_id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.body = body
