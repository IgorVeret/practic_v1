"""
В векторе повторить все значения n раз. Пример: для массива [1, 2, 3] и n равного 3, ответом
должен быть массив [1, 1, 1, 2, 2, 2, 3, 3, 3].
 """
import numpy as np


def task_2(arr, n: int) -> list:
    """
    Повторение массива
    :param arr: Массив
    :param n: Кол-во повторений
    :return: Возвращает массив повторенный указанное кол-во раз
    """
    result = np.repeat(arr, n)  # Функция repeat() повторяет элементы массива
    return list(result)


if __name__ == "__main__":
    arr = task_2(np.array([1, 2, 3]), 3)
    assert task_2(np.array([1, 2, 3]), 3) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(arr)
