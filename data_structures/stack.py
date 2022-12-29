class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавить элемент в стэк"""
        new_top = Node(data, self.top)
        self.top = new_top

    def pop(self):
        """Удалить элемент из стека и вернуть значение этого элемента"""
        if not self.top:
            return None
        popped = self.top.data
        self.top = self.top.next_node
        return popped

    def to_list(self):
        """Вернуть данные стека в виде списка"""
        lst = []
        if not self.top:
            return lst
        node = self.top
        while node:
            lst.append(node.data)
            node = node.next_node
        return lst
