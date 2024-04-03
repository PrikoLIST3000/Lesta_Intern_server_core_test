

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularBufferLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __is_empty(self):
        return self.size == 0

    def append(self, item):
        new_node = Node(item)
        if self.__is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def get(self):
        if self.__is_empty():
            raise Exception("Queue is empty!")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item


"""
Плюсы:
    1)Простота реализации
    2)Эффективность: Операции доступа к элементам списка имеют сложность O(1),
    поэтому эта реализация эффективна.
Минусы:
    1)Фиксированный размер
"""
