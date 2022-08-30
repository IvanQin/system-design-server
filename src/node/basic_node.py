from .i_node import INode
from ..communication.model.message import Message
from src.logger import Logger
from threading import Thread
from src.utils.repeated_task import RepeatedTask
from src.cluster.cluster_manager import ClusterManager

class BasicNode(INode):
    """
    Basic node will send heartbeat message to every other node and will receive heartbeat from every other nodes timely.
    """

    def __init__(self):
        super.__init__(self)
        self.working_task = None

    def set_node_id(self, node_id: str):
        self.node_id = node_id

    def get_node_id(self) -> str:
        return self.node_id

    def start(self):
        self.working_task = RepeatedTask(1, self._start())

    def _start(self):
        self.communication_mgr.send_heartbeat(self.get_node_id(), receiver_id=ClusterManager.RECEIVER_ID_ALL)

    def listen(self, message : Message):
        if message.get_receiver_id() == (ClusterManager.RECEIVER_ID_ALL or self.get_node_id()):
            Logger.i(self.get_node_id(), "listen", str(message))
