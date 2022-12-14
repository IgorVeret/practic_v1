"""Задание 5 (1 балл): Дан текст в виде строки. Напишите функцию, которая возвращает словарь,
где ключами являются уникальные слова из этого текста, а значениями - число раз,
которое данное слово встретилось в тексте. Считать, что слова разделяются пробелами.
Предложите как минимум два различных решения."""

text = 'дан текст в виде строки напишите функцию которая возвращает словарь \
в виде строки напишите функцию которая Возвращает Словарь словарь'


# 1 Вариант
def task_05_func(text: str) -> dict:
    """
    Функция  возвращает словарь, где ключами являются уникальные слова
    из этого текста, а значениями - число раз, которое данное слово встретилось в тексте.
    Вариант 1.
    :param text: Принимает строку
    :return: Возвращает словарь
    """
    text = str.lower(text)  # убираем заглавные буквы
    dict = {}  # пустой словарь

    for key in text.split():
        dict[key] = dict.setdefault(key, 0) + 1

    return dict


# 2 Вариант
def task_05_func_1(text: str) -> dict:
    """
    Функция  возвращает словарь, где ключами являются уникальные слова
    из этого текста, а значениями - число раз, которое данное слово встретилось в тексте.
    Вариант 2.
    :param text: Принимает строку
    :return: Возвращает словарь
    """
    text = str.lower(text)
    list_value = text.split()
    dict = {}

    for i in list_value:
        if not i in dict:
            dict[i] = 0
        dict[i] += 1

    return dict


if __name__ == "__main__":
    result = task_05_func(text)
    print('Вариант1', result)
    result = task_05_func_1(text)
    print('Вариант2', result)
