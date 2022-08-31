from src.node.node import Node
from src.node.node_factory import NodeFactory
from src.cluster.cluster_manager import ClusterManager
import unittest

class NodeFactoryTest(unittest.TestCase):

    def test_create_node(self):
        cluster_mgr = ClusterManager()
        node_factory = NodeFactory(cluster_mgr)
        node = node_factory.create_node()
        self.assertIsNone(node.get_node_id())
        node_factory.activate_node(node)
        self.assertIsNotNone(node.get_node_id())

    def test_create_basic_node(self):
        cluster_mgr = ClusterManager()
        node_factory = NodeFactory(cluster_mgr)
        basic_node = node_factory.create_basic_node()
        self.assertIsNone(basic_node.get_node_id())
        node_factory.activate_node(basic_node)
        self.assertIsNotNone(basic_node.get_node_id())

if __name__ == '__main__':
    unittest.main()
