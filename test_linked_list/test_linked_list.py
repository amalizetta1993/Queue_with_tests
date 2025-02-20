import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LinkedListClass import *

class TestNode(unittest.TestCase):
   
    def test_init(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.next_node, node_1)
        self.assertEqual(node_2.next_node.data, 5)