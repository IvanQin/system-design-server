from .i_node import INode

class Node(INode):

    def get_node_id(self) -> str:
        return self.node_id

    def start(self):
        pass
