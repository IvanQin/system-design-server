from src.node.interface.i_node import INode
from typing import List
from src.logger.logger import Logger
import uuid

TAG = "ClusterManager"

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
        Logger.d(TAG, f"activate node {node_id}")
        return node_id

    def get_active_nodes(self) -> List[INode]:
        active_nodes = list(self.id_to_node.values())
        Logger.d(TAG, f"return activate nodes {active_nodes}")
        return active_nodes

    def shutdown_all_nodes(self):
        for node in self.id_to_node.values():
            Logger.d(TAG, f"shutting down node [{node.get_node_id()}]")
            node.stop()
