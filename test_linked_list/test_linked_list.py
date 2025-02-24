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
            
class TestLinkedList(unittest.TestCase):
   
    def test1_insert_at_head(self):
        list1 = LinkedList()
        list1.insert_at_head('f')
        self.assertEqual(list1.head.data, 'f')
        list1.insert_at_head('g')
        self.assertEqual(list1.head.data, 'g')
        list1.remove_node_position(2)
        list1.remove_node_position(1)
        
    def test2_insert_at_end(self):
        list1 = LinkedList()
        list1.insert_at_end('f')
        self.assertEqual(list1.head.data, 'f')
        list1.insert_at_end('g')
        self.assertEqual(list1.head.next_node.data, 'g')
        list1.remove_node_position(2)
        list1.remove_node_position(1)    
        
    def test3_remove(self):
        list1 = LinkedList()
        list1.insert_at_end('f')
        list1.insert_at_end('g')
        list1.insert_at_end('s')
        self.assertEqual(list1.remove_node_position(10), 'Ничего не удалено')
        list1.remove_node_position(2)
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        
    def test4_insert_at_position(self):
        list1 = LinkedList()
        list1.insert_at_position('f',1)
        list1.insert_at_position('g',2)
        list1.insert_at_position('s',3)
        list1.insert_at_position('d',2)
        self.assertEqual(list1.head.next_node.data, 'd')
        self.assertEqual(list1.insert_at_position('d',10), None)
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        
    def test5_print(self):
        list1 = LinkedList()
        list1.insert_at_end('f')
        list1.insert_at_end('g')
        list1.insert_at_end('s')
        self.assertEqual(list1.print_ll(), 'Данные списка выведены')
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        list1.remove_node_position(1)

        
    def test6_get(self):
        list1 = LinkedList()
        list1.insert_at_end('f')
        list1.insert_at_end('g')
        list1.insert_at_end('s')
        self.assertEqual(list1.get('g'), (True, list1.head.next_node))
        self.assertEqual(list1.get('w'), (False, None))
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        list1.remove_node_position(1) 
              
    def test7_change(self):
        list1 = LinkedList()
        list1.insert_at_end('f')
        list1.insert_at_end('g')
        list1.insert_at_end('s')
        self.assertEqual(list1.change_data('g', 'w'), "Заменены данные в узле № 2")
        self.assertEqual(list1.change_data('we', 'w'), "Данные не обнаружены")
        list1.remove_node_position(1)
        list1.remove_node_position(1)
        list1.remove_node_position(1) 