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
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} -> '
            current_node = current_node.next_node
        return output

    def __iter__(self):
        # starting with 'head', iterates over the linked list
        current = self.head
        while current is not None:
            yield current.value
            current = current.next_node

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def remove_head(self):
        return_value = None
        if self.head is not None:
            return_value = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            if self.length < 2:
                self.tail = self.head
        return return_value

    def get_max(self):
        # The max() function returns the item with the highest value
        return max(self) if self.length > 0 else None
