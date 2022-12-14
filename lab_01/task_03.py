"""Задание 3 (0.5 балла): По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой
 задачи с помощью циклов можно использовать только один цикл. Предложите как минимум два различных решения."""


def task_03_func(number: int) -> int:
    """
    функция вычисления суммы  натуралльного n
    :param number: Целое число
    :return: Сумма 1!+2!+3!+...+n!
    """

    summa = 0
    previous = 1
    for i in range(1, number + 1):
        current = previous * i
        summa += current
        previous = current

    return summa


if __name__ == "__main__":
    result = task_03_func(15)
    print('Сумма факториалов равна:', result)
