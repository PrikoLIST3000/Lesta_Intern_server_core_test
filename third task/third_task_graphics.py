import random
import time
import matplotlib.pyplot as plt


def quick_ins_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    if len(arr) <= 10:  # Порог для перехода к сортировке вставками
        return insertion_sort(arr)
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


execution_times = []

for _ in range(1000):
    arr = [random.randint(1, 1000) for _ in range(1000)]
    start_time = time.time()
    sorted_arr = quick_sort(arr)  # или quick_ins_sort
    end_time = time.time()
    execution_times.append(end_time - start_time)

plt.plot(range(1, 1001), execution_times, marker='o', linestyle='-')
plt.xlabel('Попытка')
plt.ylabel('Время выполнения (сек)')
plt.title('Время выполнения Quick Sort + Insertion Sort (1000 попыток')
plt.grid(True)
plt.savefig('quick_insertion_sort_execution_times_arrays.png')
plt.show()
