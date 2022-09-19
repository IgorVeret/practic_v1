'''Задание 1.Проверить, что все элементы входного массива строго положительны.'''
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, -2, -3, 4, 5, 6])


def task_1(arr):
    """

        Функция проверки массива на положительность
        :param year: - массив
        :return: - True or False
    """

    new = arr > 0
    return new.all()  # Обобщаем список


if __name__ == "__main__":
    arr_a = task_1(a)
    arr_b = task_1(b)
    print(arr_a)
    print(arr_b)
