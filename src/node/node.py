from .i_node import INode

class Node(INode):


    def set_node_id(self, node_id: str):
        self.node_id = node_id

    def get_node_id(self) -> str:
        return self.node_id

    def start(self):
        pass
