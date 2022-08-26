from .i_node import INode
from ..communication.model.message import Message
from src.logger import Logger

class BasicNode(INode):
    """
    Basic node will send heartbeat message to every other node and will receive heartbeat from every other nodes timely.
    """

    def set_node_id(self, node_id: str):
        self.node_id = node_id

    def get_node_id(self) -> str:
        return self.node_id

    def start(self):
        pass

    def listen(self, message : Message):
        Logger.i(self.get_node_id, str(message))
