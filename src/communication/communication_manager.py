from queue import Queue
from .model.message import Message
from .model.message_action import Action
from .model.message_body import MessageBody
from ..cluster.cluster_manager import ClusterManager

class CommunicationManager():

    def __init__(self, cluster_manager : ClusterManager) -> None:
        self.message_queue = Queue()
        self.cluster_manager = cluster_manager

    # TODO the public API here should be the specific actions from the node, Message itself should be hidden from the Node layer
    def increment_value(self, sender_id : str, receiver_id : str):
        message_body = MessageBody(Action.INCREMENT_VALUE)
        self._send_message(sender_id, receiver_id, message_body)

    def decrement_value(self, sender_id : str, receiver_id : str):
        message_body = MessageBody(Action.DECREMENT_VALUE)
        self._send_message(sender_id, receiver_id, message_body)

    def _send_message(self, sender_id : str, receiver_id : str, message_body: MessageBody):
        msg = Message(sender_id,receiver_id, message_body)
        self._put(msg)

    def _put(self, message : Message):
        self.message_queue.put(message)

    def _get(self) -> Message:
        self.message_queue.get()

    # start up a thread to call this method in a periodical way
    def _broadcast(self, message: Message):
        map(lambda node: node.listen(message), self.cluster_manager.get_active_nodes)
