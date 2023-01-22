import ctypes
from interface.sequence import Sequence


class Node:
    def __init__(self, item, next_pointer):
        self.item = item
        self.next = next_pointer


class LinkedListSequence(Sequence):
    def __init__(self, items: list):
        super(LinkedListSequence, self).__init__(items)
        self._nodes = [Node(items[0], None)]
        for item in items[1::-1]:
            next_node = self._nodes[0]
            past_node = Node(item, id(next_node))
            self._nodes.insert(0, past_node)
        self._nodes.insert(0, Node(len(items), id(self._nodes[0])))
        self.head = self._nodes[0]
        self._cursor = id(self.head)

    def __len__(self):
        return self.head.item

    def iter_seq(self):
        past_node = ctypes.cast(self._cursor, ctypes.py_object).value
        self._cursor = past_node.next
        return ctypes.cast(self._cursor, ctypes.py_object).value

    def get_at(self, i):
        pointer = self.head.next
        for i_pointer in range(i):
            next_node = ctypes.cast(pointer, ctypes.py_object).value
            pointer = next_node.next
        return ctypes.cast(pointer, ctypes.py_object).value

    def set_at(self, i, x):
        target_node = self.get_at(i)
        target_node.item = x

    def insert_at(self, i, x):
        assert i >= 0, f"Wrong index : {i}"
        if i > 0:
            past_node = self.get_at(i-1)
            next_node = self.get_at(i)
            new_node = Node(x, id(next_node))
            past_node.next = id(new_node)
        else:
            self.insert_first(x)

    def delete_at(self, i):
        assert i >= 0, f"Wrong index : {i}"
        if i > 0:
            past_node = self.get_at(i-1)
            next_node = self.get_at(i)
            past_node.next = id(next_node)
        else:
            self.delete_first()

    def insert_first(self, x):
        past_node = self.head
        next_node = self.get_at(0)
        new_node = Node(x, id(next_node))
        past_node.next = id(new_node)

    def delete_first(self):
        past_node = self.head
        next_node = self.get_at(1)
        past_node.next = id(next_node)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        self.delete_at(len(self))

