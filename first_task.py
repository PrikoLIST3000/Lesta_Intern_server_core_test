

# Реализация 1 (пример)
def isEven_1(value):
    return value % 2 == 0


"""
Плюсы:
    1)Легко читаемая и очевидная реализация
Минусы:
    1)Может быть затрано при работе с большими числами
"""


# Реализация 2
def isEven_2(value: int) -> bool:
    return value & 1 == 0


"""
Плюсы:
    1)Побитовые операции обычно выполняются быстрее
Минусы:
    1)Вызывает некоторые вопросы у тех, кто читает твой код, потому что могут не знать о таком подходе
"""
