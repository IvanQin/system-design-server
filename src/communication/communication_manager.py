from queue import Queue
from .model.message import Message
from .model.message_action import Action
from .model.message_body import MessageBody
from ..cluster.cluster_manager import ClusterManager
from ..utils.repeated_task import RepeatedTask
from src.logger.logger import Logger

TAG = "CommunicationManager"

class CommunicationManager():

    def __init__(self, cluster_manager : ClusterManager) -> None:
        self.message_queue = Queue()
        self.cluster_manager = cluster_manager
        self.broadcast_service = None
        self.is_running = False

    def start_service(self):
        Logger.d(TAG, "start service")
        if self.is_running:
            return
        self.is_running = True
        self.broadcast_service = RepeatedTask(0.5, self._broadcast)
        self.broadcast_service.start()

    def end_service(self):
        Logger.d(TAG, "end service")
        if self.broadcast_service:
            self.broadcast_service.stop()
        self.is_running = False

    # TODO the public API here should be the specific actions from the node, Message itself should be hidden from the Node layer
    def increment_value(self, sender_id : str, receiver_id : str):
        message_body = MessageBody(Action.INCREMENT_VALUE)
        self._send_message(sender_id, receiver_id, message_body)

    def decrement_value(self, sender_id : str, receiver_id : str):
        message_body = MessageBody(Action.DECREMENT_VALUE)
        self._send_message(sender_id, receiver_id, message_body)

    def send_heartbeat(self, sender_id : str, receiver_id : str):
        message_body = MessageBody(Action.HEARTBEAT)
        self._send_message(sender_id, receiver_id, message_body)

    def _send_message(self, sender_id : str, receiver_id : str, message_body: MessageBody):
        msg = Message(sender_id,receiver_id, message_body)
        Logger.d(TAG, f'send message {str(msg)}')
        self._put(msg)

    def _put(self, message : Message):
        self.message_queue.put(message)

    def _get(self) -> Message:
        return None if self.message_queue.empty() else self.message_queue.get_nowait()

    def _broadcast(self):
        Logger.d(TAG, 'internal broadcast called')
        message = self._get()
        if message:
            Logger.d(TAG, f'broadcast message {str(message)}')
            for node in self.cluster_manager.get_active_nodes():
                node.listen(message)
