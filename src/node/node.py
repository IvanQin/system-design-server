from .i_node import INode
from ..communication.model.message import Message

class Node(INode):


    def set_node_id(self, node_id: str):
        self.node_id = node_id

    def get_node_id(self) -> str:
        return self.node_id

    def start(self):
        pass

    def listen(self, message : Message):
        pass
