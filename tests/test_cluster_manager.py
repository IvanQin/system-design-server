from src.cluster.cluster_manager import ClusterManager
from src.node.node_factory import NodeFactory
import unittest

class ClusterManagerTest(unittest.TestCase):

    def test_get_activated_nodes(self):
        cluster_mgr = ClusterManager()
        node_factory = NodeFactory(cluster_mgr)
        node1 = node_factory.create_node()
        node2 = node_factory.create_node()

        node_factory.activate_node(node1)
        node_factory.activate_node(node2)

        active_nodes = cluster_mgr.get_active_nodes()
        self.assertEqual(len(active_nodes), 2)
        self.assertEqual(active_nodes[0], node1)
        self.assertEqual(active_nodes[1], node2)

if __name__ == '__main__':
    unittest.main()
