class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Добавить данные в очередь"""
        if not self.head and not self.tail:
            self.tail = self.head = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def dequeue(self):
        """Забрать данные из очереди"""
        if not self.head:
            return None
        popped = self.head.data
        self.head = self.head.next_node
        if not self.head:
            self.tail = None
        return popped

    def to_list(self):
        """Вернуть данные очереди в виде списка"""
        lst = []
        if not self.head:
            return lst
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next_node
        return lst
