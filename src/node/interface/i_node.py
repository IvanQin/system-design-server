from abc import ABC, abstractmethod
from src.communication.model.message import Message
from src.communication.communication_manager import CommunicationManager
class INode(ABC):

    def __init__(self, node_id : str = None, communication_mgr : CommunicationManager = None):
        self.node_id = node_id
        self.communication_mgr = communication_mgr

    @abstractmethod
    def set_node_id(self, node_id: str):
        raise NotImplementedError()

    @abstractmethod
    def get_node_id(self)-> str :
        raise NotImplementedError()

    @abstractmethod
    def start(self):
        raise NotImplementedError()

    @abstractmethod
    def listen(self, message : Message):
        raise NotImplementedError()
