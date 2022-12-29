class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self):
        """Возвращает список, содержащий данные узлов связанного списка"""
        lst = []
        if not self.head:
            return lst
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next_node
        return lst

    def print_ll(self):

        if self.head:
            current_node = self.head
        elif self.tail:
            current_node = self.tail
        else:
            return 'None'

        node_data = []

        while current_node.next_node:
            node_data.append(current_node.data)
            current_node = current_node.next_node

        node_data.append(current_node.data)
        node_data.append(None)

        return ' -> '.join(map(str, node_data))

    def insert_beginning(self, data):
        """Добавить данные в началов связанного списка"""
        if self.head is None:
            self.head = self.tail = Node(data, None)
            return
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        """Добавить данные в конец связанного списка"""
        if self.head is None:
            self.head = self.tail = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def get_vacancy_by_id(self, vacancy_id):
        """Получить данные из связанного списка по id"""
        node = self.head
        while node:
            if node.data['id'] == vacancy_id:
                return node.data
            node = node.next_node
        return None
