from abc import ABC, abstractmethod

class INode(ABC):

    def __init__(self, node_id : str = None):
        self.node_id = node_id

    @abstractmethod
    def set_node_id(self, node_id: str):
        raise NotImplementedError()
    
    @abstractmethod
    def get_node_id(self)-> str :
        raise NotImplementedError()

    @abstractmethod
    def start(self):
        raise NotImplementedError()
