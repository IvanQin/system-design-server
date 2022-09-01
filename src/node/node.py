from src.node.interface.i_node import INode
from src.communication.model.message import Message
from src.communication.communication_manager import CommunicationManager

class Node(INode):

    def set_communication_mgr(self, communication_manager : CommunicationManager):
        self.communication_mgr = communication_manager

    def set_node_id(self, node_id: str):
        self.node_id = node_id

    def get_node_id(self) -> str:
        return self.node_id

    def start(self):
        pass

    def stop(self):
        pass

    def listen(self, message : Message):
        pass
