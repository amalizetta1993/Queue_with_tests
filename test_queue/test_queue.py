import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from queue_1 import Queue

class TestQueue(unittest.TestCase):
   
    def test_IsEmpty(self):
        q = Queue(8, ['fd'])
        self.assertEqual(q.isEmpty(), False)
        q.dequeue()
        self.assertEqual(q.isEmpty(), True)
             
    def test_IsFull(self):
        q = Queue(3, ['fd', 'fdf', 'gvf'])
        self.assertEqual(q.isFull(), True)
        q.dequeue()
        self.assertEqual(q.isEmpty(), False)
        

