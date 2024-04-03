import random

random.seed(43)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) <= 10:  # Порог для перехода к сортировке вставками
        return insertion_sort(arr)
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


"""
    Здесь я использую Быструю сортировку (Quick Sort) в комбинации с Сортировкой вставками (Insertion sort)
    Quick Sort один из самых быстрых алгоритмов в среднем случае и хорошо работает с большими массивами данных,
    а Insertion Sort хорошо работает с небольшими массивами данных, проверил на своём ПК, вроде бы этот гибрид
    получился быстрее обычной быстрой сортировки
"""
