from node.node import Node
import uuid
class ClusterManager():

    def __init__(self):
        self.id_to_node = {}

    def activate(self, node : Node) -> str:
        """
        activate the node and get back a node_id
        """
        node_id = str(uuid.uuid4())
        self.id_to_node[node_id] = node
        return node_id