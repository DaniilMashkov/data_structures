class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Дабавляет в бинарное дерево поиска новый узел с данными Node(data)"""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rec(data, self.root)

    def _insert_rec(self, data, node):
        if data.get('id') < node.data.get('id'):
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_rec(data, node.left)

        elif data.get('id') > node.data.get('id'):
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_rec(data, node.right)

    def search(self, data):
        """
            Возвращает данные о вакансии с полем id, равным vacancy_id.
            Возвращает False, если нет вакансии с id, равным vacancy_id.
        """

        if self.root is None:
            return False
        return self._search_rec(data, self.root)

    def _search_rec(self, data, node):
        if node is None:
            return False

        if data == node.data.get('id'):
            return node.data

        if data < node.data.get('id'):
            return self._search_rec(data, node.left)

        if data > node.data.get('id'):
            return self._search_rec(data, node.right)