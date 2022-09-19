"""Задание 15 (1.5 балла): Написать функцию, которая во входной строке заменяет вхождения всех
английских заглавных букв на их номер в таблице ASCII, затем производит сплит по минимальной
из цифр строки. Предложите как минимум два различных решения, одно из которых не должно
использовать циклы. При  использовании циклов допускается не более двух проходов по строке."""

import re


# Вариант 1
def task_15_func1(n: str) -> list:
    """
    Функция заменяет заглавные буквы на номер таблицы ASCII
    про зводит сплит по минимальной из цифр строки. Возвращает список. Вариант 1.
    :param n: Принимает строку
    :return: Возвращает список
    """
    spisok = []  # Список
    for i in n:  # Проверям на заглавные буквы и преобразуем в список
        if i.isupper():

            spisok.append(str(ord(i)))  # Заменяем заглавные буквы

        else:
            spisok.append(i)
    stroka_new = ''.join(spisok)  # Превращаем список в строку
    number_find = re.findall('[1-9]', stroka_new)  # Поиск числа в строке
    min_number = min(number_find)  # Находим минимальное число
    result = stroka_new.split(sep=min_number)  # Сплитуемся по минимальному числу
    return result


def task_15_func2(m: str) -> list:
    """
    Функция заменяет заглавные буквы на номер таблицы ASCII
    про зводит сплит по минимальной из цифр строки. Возвращает список. Вариант 2.
    :param n: Принимает строку
    :return: Возвращает список
    """
    stroka_new = "".join(map(lambda ch: str(ord(ch)) if ch.isascii() and ch.isupper() else ch, m))
    min_number = min(filter(lambda x: x.isdigit(), stroka_new))

    result = stroka_new.split(str(min_number))
    return result


if __name__ == "__main__":
    func_1 = task_15_func1('In Google Chrome the 1 address bar  that sits at the top of the browser  Window')
    func_2 = task_15_func2('In Google 1  Chrome the address bar  that sits at 2 the top of the browser  window')
    print('Вариант 1', func_1)
    print('Вариант 2', func_2)
