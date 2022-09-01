from src.cluster.cluster_manager import ClusterManager
from src.node.node_factory import NodeFactory
from src.communication.communication_manager import CommunicationManager
import time

def start():
    # setup components
    cluster_manager = ClusterManager()
    node_factory = NodeFactory(cluster_manager)
    communication_manager = CommunicationManager(cluster_manager)

    nodeA = node_factory.create_basic_node()
    nodeB = node_factory.create_basic_node()

    node_factory.activate_node(nodeA)
    node_factory.activate_node(nodeB)
    nodeA.set_communication_mgr(communication_manager)
    nodeB.set_communication_mgr(communication_manager)

    communication_manager.start_service()
    nodeA.start()
    nodeB.start()

    time.sleep(5)

    communication_manager.end_service()
    cluster_manager.shutdown_all_nodes()

if __name__ == '__main__':
    start()
