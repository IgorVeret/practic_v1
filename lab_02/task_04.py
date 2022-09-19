"""Задание 4 (2 балл): Опишите декоратор, который принимает на вход функцию и при каждом
 её вызове печатает строку "This function was called N times", где N - число раз, которое
 это функция была вызвана на текущий момент (пока функция существует как объект, это число,
 очевидно, может только неубывать)."""


def calls_counter(func):
    """
    
    :param func: Принимает на вход функцию
    :return: None
    """
    func.count = 0

    def wrap(*args):
        """

        :param args: Функция подсчитывает кол-во обращений
        :return:
        """
        func.count += 1
        print('Эта функция вызывалась {} раз'.format(func.count))

    return wrap


@calls_counter
def func(a):
    pass


if __name__ == "__main__":
    for a in range(4):  # число повторений
        func(a)
