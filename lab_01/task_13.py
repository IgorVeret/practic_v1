"""Задание 13 (1 балл): Написать функцию, которая принимает на вход число n, которое может
быть либо натуральным, либо -1, и возвращает генератор чисел Фиббоначи. Если входной параметр
равен натуральному числу, то генератор должен выдавать последовательно числа Фиббоначи до n-го.
 Если n равно -1, то генератор должен быть бесконечным."""


def task_13_func(n: int) -> list:
    """
    Функция возвращает список чисел Фиббоначи.
    :param n: Целое число n
    :return: Числа фибоначм до n-го
    """
    a = 0
    b = 1
    if n > 0:

        for __ in range(n):
            yield a
            a, b = b, a + b

    elif n == -1:
        while b >= 1:
            yield a
            a, b = b, a + b

    elif n < -1:
        n = 'Число не в диапазоне от бесконечности до -1'

        return n


def test(n: int) -> list:
    z = list(task_13_func(n))

    return z


if __name__ == "__main__":
    result = test(10)  # число n
    print(result)
