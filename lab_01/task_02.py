"""Задание 2 (0.5 балла): Дано натуральное число. Найдите число знаков в его десятичной записи.
Предложите как минимум два различных решения."""


# Первый способ
def task_02_func_01(number: int) -> int:
    """
    Функция подсчета числа знаков
    :param number:  целое число
    :return: число знаков в числе
    записи. Вариант 1
    """
    number = str(number)

    return len(number)


# Второй способ
def task_02_func_02(value: int) -> int:
    """
    Функция подсчета числа знаков
    :param number:  целое число
    :return: число знаков в числе
    записи. Вариант 2
    """
    item = 0
    while value > 0:
        value = value // 10
        item += 1

    return item


if __name__ == "__main__":
    func_1 = task_02_func_01(1607)
    print('Количество знаков равно', func_1)
    func_2 = task_02_func_02(1807)
    print('Количество знаков равно', func_2)
