'''Задание 6 (1 балл): Напишите функцию, которая принимает на вход строку и символ и возвращает:
- если символ встретился в строке один раз - кортеж (индекс вхождения, None);
- если два и более раз - кортеж (индекс первого вхождения, индекс последнего вхождения);
- если ни разу - кортеж (None, None).
Запрещается делать более одного прохода по каждому элементу строки.'''


def task_06_func(input_str: str, input_char: str) -> tuple:
    """
    Функция  принимает на вход строку и символ и возвращает:
    - если символ встретился в строке один раз - кортеж (индекс вхождения, None);
    - если два и более раз - кортеж (индекс первого вхождения, индекс последнего вхождения);
    - если ни разу - кортеж (None, None)
    :param input_str: Принимает строку
    :param input_char: Принимает символ
    :return: Возвращает кортеж
    """
    fst_id, sec_id = (None, None)  # Возврщаем если символ не обнаружен
    for i, c in enumerate(input_str):
        if c == input_char:
            if fst_id is None:
                fst_id = i
            else:
                sec_id = i
    return fst_id, sec_id


if __name__ == "__main__":
    input_str = 'во поле березка стояла э'
    input_char = 'э'
    result = task_06_func(input_str, input_char)
    print(result)

    # Проверка на наличие символа одного символа
    input_str1 = 'во поле березка стояла э'
    input_char1 = 'э'
    assert task_06_func(input_str1, input_char1) == (23, None)

    # Проверка на наличие двух и более символов
    input_str2 = 'во поле березка стояла э'
    input_char2 = 'е'
    assert task_06_func(input_str2, input_char2) == (6, 11)

    # Проверка на отсутствии символов
    input_str3 = 'во поле березка стояла э'
    input_char3 = 'ю'
    assert task_06_func(input_str3, input_char3) == (None, None)
