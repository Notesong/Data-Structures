"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} -> '
            current_node = current_node.next
        return output

    def __len__(self):
        return self.length

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            print("-in __iter__ - current_node.value: ", current_node.value)
            current_node = current_node.next

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.head is None and self.tail is None:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1
        print("-in add to head: ", self)

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is None:
            return None
        old_head = self.head.value
        self.delete(self.head)
        return old_head
        print("-in remove from head: ", self)

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.head is None and self.tail is None:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1
        print("-in add to tail: ", self)

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.tail is None:
            return None
        old_tail = self.tail.value
        self.delete(self.tail)
        return old_tail
        print("-in remove from tail: ", self)

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.tail:
            self.tail = self.tail.prev
        node_value = node.value
        node.delete()
        self.add_to_head(node_value)
        self.length -= 1
        print("-in move to front: ", self)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.head:
            self.head = self.head.next
        node_value = node.value
        node.delete()
        self.add_to_tail(node_value)
        self.length -= 1
        print("-in move to end: ", self)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        if self.head is node:
            self.head = self.head.next
        elif self.tail is node:
            self.tail = self.tail.prev
        node.delete()
        self.length -= 1
        if len(self) is 0:
            self.head = None
            self.tail = None
        print("-in delete: ", self)

    """Returns the highest value currently in the list"""

    def get_max(self):
        print("-in get_max: ", self)
        return max(self) if self.length > 0 else None
