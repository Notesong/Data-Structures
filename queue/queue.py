"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

    Arrays use indexes to find the head to add or remove an item, whereas a linked 
    list uses the pointers to find it.  Arrays also take care of their own lengths
    so it's not necessary to keep track of them like it is in a queue.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import SinglyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = SinglyLinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add the new value to the tail of our list
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        # remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()
        return value
