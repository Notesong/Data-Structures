"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   Arrays use indexes to find the head to add or remove an item, whereas a linked 
   list uses the pointers to find it. Arrays also take care of their own lengths
    so it's not necessary to keep track of them like it is in a stack.

"""

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = SinglyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # increase the size of the stack by one
        self.size += 1
        # add an element to the front of the linked list
        self.storage.add_to_head(value)

    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # decrement the size of the stack by one
        self.size -= 1
        # remove the first element in storage and return the removed head
        node = self.storage.remove_head()
        return node