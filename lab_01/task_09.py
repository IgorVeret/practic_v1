"""Задание 9 (1 балл): Напишите функцию, которая получает на вход натуральное число n и
выводит первые n строк треугольника Паскаля."""


def task_09_func(number: list) -> list:
    """
    Функция возвращает строки треугольника Паскаля
    :param number: Принимает список
    :return: Возвращает список, строки треугольника Паскаля
    """
    number = [1] + number
    for i in range(1, len(number) - 1):
        number[i] += number[i + 1]

    return number


if __name__ == "__main__":
    number = []
    for i in range(10):  # Передаем натуральное число n
        number = task_09_func(number)
        print(number)
