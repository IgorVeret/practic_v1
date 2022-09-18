"""Задание 1 (0.5 балла): Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если год является високосным,
то выведите YES, иначе выведите NO. Напомним, что в соответствии с
григорианским календарем, год является високосным, если его номер кратен 4,
но не кратен 100, а также если он кратен 400."""


def task_01_func(year: int) -> str:
    """

        функция проверки года на високосность
        :param year: - год для проверки
        :return: - result("YES" or "NO")
    """

    return "YES" if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else "NO"


if __name__ == "__main__":
    result = task_01_func(2044)
    print(result)
