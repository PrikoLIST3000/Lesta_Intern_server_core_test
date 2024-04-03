

class CircularBufferList:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__buffer = [None] * capacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __is_empty(self):
        return self.__size == 0

    def __is_full(self):
        return self.__size == self.__capacity

    def append(self, item):
        if self.__is_full():
            raise Exception("Queue is full!")
        self.__buffer[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__size += 1
        return True

    def get(self):
        if self.__is_empty():
            raise Exception("Queue is empty!")
        item = self.__buffer[self.__head]
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        return item


"""
Плюсы:
    1)Динамический размер
    2)Вставка и удаление элементов в связанном списке имеют сложность O(1)
Минусы:
    1)Дополнительное использование памяти для каждого из узлов элемента
"""
