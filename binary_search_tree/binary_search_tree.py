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

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = SinglyLinkedList()

    def __len__(self):
        # returns the length of the queue
        return self.size

    def enqueue(self, value):
        # increase the size of the queue by one
        self.size += 1
        # add the new value to the tail of our list
        self.storage.add_to_tail(value)

    def dequeue(self):
        # return 0 if nothing is in the queue
        if self.size == 0:
            return None
        # decrement the size of the queue by one
        self.size -= 1
        # remove the value from the head of our list and return the value of the
        # removed head
        value = self.storage.remove_head()
        return value


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        does_contain = False
        if self.value == target:
            does_contain = True
        elif target < self.value:
            if self.left is None:
                does_contain = False
            else:
                does_contain = self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                does_contain = False
            else:
                does_contain = self.right.contains(target)
        return does_contain

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.for_each(print)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = Queue()
        # add the first node to the queue
        queue.enqueue(node)
        # while the stack is not empty
        while len(queue) > 0:
            # remove the first node from the queue
            current_node = queue.dequeue()
            # print the value of the removed node
            print(current_node.value)
            # add all children into the queue
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = Stack()
        # add the first node to the stack
        stack.push(node)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            current_node = stack.pop()
            # print that node
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
