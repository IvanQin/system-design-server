from src.node.interface.i_node import INode
from typing import List
import uuid
class ClusterManager():

    RECEIVER_ID_ALL = "0"

    def __init__(self):
        self.id_to_node = {}

    def activate(self, node : INode) -> str:
        """
        activate the node and get back a node_id
        """
        node_id = str(uuid.uuid4())
        self.id_to_node[node_id] = node
        return node_id

    def get_active_nodes() -> List[INode]:
        return self.id_to_node.values()
