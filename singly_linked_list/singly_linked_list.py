class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        # starting with 'head', iterates over the linked list
        # prints out the nodes in the list one by one
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} -> '
            current_node = current_node.next_node
        return output

    def __iter__(self):
        # starting with 'head', iterates over the linked list
        # returns the value of each node
        # In this class, this function is used by max() to get the
        # largest number contained in the nodes
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next_node

    def __len__(self):
        # returns the length of the linked list
        return self.length

    def add_to_head(self, value):
        # sets up the new node
        new_node = Node(value)
        # if there are no nodes in the linked list, made the new
        # node the head and tail of the linked list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if there is at least one node, set the new_node's next_node
        # to be the current head and then set the head to be the new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        # add one to the linked list's length
        self.length += 1

    def add_to_tail(self, value):
        # sets up the new node
        new_node = Node(value)
        # if there are no nodes in the linked list, made the new
        # node the head and tail of the linked list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if there is at least one node, set the current tail's next_node
        # to be the new_node and then set the tail to be the new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        # add one to the linked list's length
        self.length += 1

    def contains(self, value):
        # if there are no nodes, return false
        if self.head is None:
            return False
        # set current_node to be the head of the linked list
        current_node = self.head
        # starting with 'head', iterates over the linked list
        # if the value is found in the linked list, return true
        # otherwise, after the iteration is done, return false
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def remove_head(self):
        # this statement will make the return statement below return none 
        # if there isn't a head node
        return_value = None
        # if there is a head node
        if self.head is not None:
            # set the return_value to the head's value
            return_value = self.head.value
            # set the head to the next node in the linked list
            self.head = self.head.next_node
            # take away 1 from the length of the linked list
            self.length -= 1
            # if there is only one node, attach the tail to the head
            if self.length < 2:
                self.tail = self.head
        # return the removed head's value or none if there are no nodes in
        # the linked list 
        return return_value

    def get_max(self):
        # The max() function returns the item with the highest value
        # this function uses the custom __iter__ function above to iterate 
        # over the nodes
        # if the length of the linked list is 0, return None
        return max(self) if self.length > 0 else None
