from src.node.node import Node
import unittest

class NodeTest(unittest.TestCase):

    def test_create_node(self):
        node1 = Node("node_1")
        self.assertEqual(node1.get_node_id(), "node_1")

if __name__ == '__main__':
    unittest.main()
