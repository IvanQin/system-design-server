from src.node.node import Node
from src.node.basic_node import BasicNode
import unittest

class NodeTest(unittest.TestCase):

    def test_create_node(self):
        node1 = Node("node_1")
        self.assertEqual(node1.get_node_id(), "node_1")

    def test_create_basic_node(self):
        basic_node = BasicNode("basic_node")
        self.assertEqual(basic_node.get_node_id(), "basic_node")


if __name__ == '__main__':
    unittest.main()
