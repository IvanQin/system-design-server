from queue import Queue
from .model.message import Message
from .model.message_action import Action
from .model.message_body import MessageBody

class CommunicationManager():

    def __init__(self) -> None:
        self.message_queue = Queue()

    # TODO the public API here should be the specific actions from the node, Message itself should be hidden from the Node layer

    def _send_message(self, sender_id : str, receiver_id : str, message_body: MessageBody): 
        msg = Message(sender_id,receiver_id, message_body)
        pass

    def _put(self, message : Message):
        self.message_queue.put(message)

    def _get(self) -> Message:
        self.message_queue.get()

        