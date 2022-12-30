class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        """Возвращает целове число (хеш-значение), находящийся в пределах от 0 до table_size"""
        hash_value = 0
        for sym in key:
            hash_value += ord(sym)
            hash_value = (hash_value * ord(sym)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        """
        Добавить новый узел Node(Data(key, value) в хеш-таблицу hash_table[hashed_key]=Node(...)
        При возникновении коллизии строится связанный список.
        """
        hash_key = self.custom_hash(key)
        if self.hash_table[hash_key] is None:
            self.hash_table[hash_key] = Node(Data(key, value), None)
            return
        node = self.hash_table[hash_key]
        while node.next_node:
            if node.data.key == key:
                node.data.value = value
                return
            node = node.next_node
        if node.data.key == key:
            node.data.value = value
            return
        node.next_node = Node(Data(key, value), None)

        # while current_node.next_node:
        #     if current_node.data.key == key:
        #         current_node.data.value = value;
        #         return
        #     current_node = current_node.next_node

    def get_value(self, key):
        """Получить значение (атрибут value класса Data) по ключу key"""
        hash_key = self.custom_hash(key)
        node = self.hash_table[hash_key]
        if node is None:
            return None
        while node.next_node:
            if key == node.data.key:
                return node.data.value
            node = node.next_node
        return node.data.value




