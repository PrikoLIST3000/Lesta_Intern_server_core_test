

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularBufferLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __is_empty(self):
        return self.__size == 0

    def append(self, item):
        new_node = Node(item)
        if self.__is_empty():
            self.__head = new_node
        else:
            self.__tail.next = new_node
        self.__tail = new_node
        self.__size += 1

    def get(self):
        if self.__is_empty():
            raise Exception("Queue is empty!")
        item = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return item


"""
Плюсы:
    1)Простота реализации
    2)Эффективность: Операции доступа к элементам списка имеют сложность O(1),
    поэтому эта реализация эффективна.
Минусы:
    1)Фиксированный размер
"""
