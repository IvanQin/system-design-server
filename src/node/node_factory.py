from cluster.cluster_manager import ClusterManager
from src.node.node import Node

class NodeFactory():
    def __init__(self, cluster_manager: ClusterManager):
        self.cluster_manager = cluster_manager

    def create_node(self) -> Node:
        return Node()

    def activate_node(self, node: Node):
        node_id = self.cluster_manager.activate(node)
        node.set_node_id(node_id)
