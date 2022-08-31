from src.cluster.cluster_manager import ClusterManager
from src.node.node import Node
from src.node.basic_node import BasicNode
from src.node.interface.i_node import INode

class NodeFactory():
    def __init__(self, cluster_manager: ClusterManager):
        self.cluster_manager = cluster_manager

    def create_node(self) -> Node:
        return Node()

    def create_basic_node(self) -> BasicNode:
        return BasicNode()

    def activate_node(self, node: INode):
        node_id = self.cluster_manager.activate(node)
        node.set_node_id(node_id)
