## Задание 1
<details>
  <summary>Условие задания</summary>

На языке Python или С/С++, написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.

Объяснить плюсы и минусы обеих реализаций.
</details>

Решение: [ссылка](https://github.com/PrikoLIST3000/Lesta_Intern_server_core_test/blob/main/first_task.py)

## Задание 2

<details>
  <summary>Условие задания</summary>
На языке Python или С++ написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
Оценивается:
Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
</details>



1. Реализация на статическом массиве: [ссылка](https://github.com/PrikoLIST3000/Lesta_Intern_server_core_test/blob/main/second%20task/second_class.py);

2. Реализация с помощью связных списков на динамическом массиве: [ссылка](https://github.com/PrikoLIST3000/Lesta_Intern_server_core_test/blob/main/second%20task/first_class.py).



## Задание 3

<details>
  <summary>Условие задания</summary>

На языке Python или С++ предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. 
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
</details>
    Здесь я использую Быструю сортировку (Quick Sort) в комбинации с Сортировкой вставками (Insertion sort)
    Quick Sort один из самых быстрых алгоритмов в среднем случае и хорошо работает с большими массивами данных,
    а Insertion Sort хорошо работает с небольшими массивами данных, проверил на своём ПК, вроде бы этот гибрид
    получился быстрее обычной быстрой сортировки
    
Решение: [ссылка](https://github.com/PrikoLIST3000/Lesta_Intern_server_core_test/blob/main/third%20task/third_task.py)

Там так же лежит 4 скриншота, где я проверял, быстрее ли эта гибридная сортировка по сравнению с обычной Быстрой сортировкой
4 случая:
1)Случайные 1000 массивов длинной в 1000 элементов для Quick Sort
2)Сидированные 1000 массивов длинной в 1000 элементов для Quick Sort
3)Те же сидированные 1000 массивов длинной в 1000 элементов для Quick Sort + Insertion sort
4)Случайные 1000 массивов длинной в 1000 элементов для Quick Sort + Insertion sort
