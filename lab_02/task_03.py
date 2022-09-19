"""Задание 3 (2 балла): Опишите класс для векторов в N-мерном пространстве.
В качестве основы используйте список значений координат вектора, задаваемый list.
Обеспечьте поддержку следующих операций: сложение, вычитание (с созданием нового вектора-результата),
скалярное произведение, косинус угла, евклидова норма. Все операции, которые можно перегрузить
с помощью магических методов, должны быть реализованы именно через них. Класс должен производить
проверку консистентности аргументов для каждой операции и в случаях ошибок выбрасывать исключение
ValueError с исчерпывающим объяснением ошибки."""

import math


class Vector:
    """

            Класс получает список и обеспечивает операции
            сложение, вычитание (с созданием нового вектора-результата),
            скалярное произведение, косинус угла, евклидова норма.
    """

    def __init__(self, vector_values_list: list):
        if len(vector_values_list) == 0:
            raise ValueError("Пустой список")

        self.v = vector_values_list

    def __check(self, other):
        """
            Метод выполняет проверку на длинну векторов.
            Если она разная, пишется исключение.
        """
        if len(self.v) != len(other.v):  # Проверяем длинну списков
            raise ValueError("Векторы имеют разное количество\
             координат: {} != {}".format(len(self.v), len(other.v)))
        return True

    def __add__(self, other):
        """

            Все операции, которые можно перегрузить
            с помощью магических методов
        """
        if self.__check(other):  # Проверяем длинну списков
            new_v = []  # Создаем новый вектор
            for i in enumerate(self.v):
                new_v.append(self.v[i[0]] + other.v[i[0]])

        return new_v

    def __sub__(self, other):
        if self.__check(other):
            new_v = []
            for i in enumerate(self.v):
                new_v.append(self.v[i[0]] - other.v[i[0]])

        return new_v

    def __mul__(self, other):
        if self.__check(other):
            new_v = 0
            for i in enumerate(self.v):
                new_v += self.v[i[0]] * other.v[i[0]]

        return new_v

    @property
    def length(self):
        """
            Метод вычисляет длинну вектора
        """
        l = 0
        for i in self.v:
            l += i ** 2
        length_vector = math.sqrt(l)
        return length_vector


if __name__ == "__main__":
    try:
        vector_a = Vector([2, 3, 5, 8, 9, ])  # Вектор 1
        vector_b = Vector([3, 4, 5, 10, 15, ])  # Вектор 2
    except NameError:
        print("Работа программы некорректна. Введеный вектор имеет неподдерживаемые\
         символы или буквы.")

    sum = vector_a + vector_b
    residual = vector_a - vector_b
    multiplication = vector_a * vector_b
    cos = (vector_a * vector_b) / (vector_a.length * vector_b.length)
    print('Сумма векторов =', sum)
    print('Разность векторов =', residual)
    print('Скалярное произведение =', multiplication)
    print('Косинус угла =', cos)
    print(f'Длинна вектора vector_a = {vector_a.length} (Евклидова норма)')
    print(f'Длинна вектора vector_b = {vector_b.length} (Евклидова норма)')

    vector_c = Vector([1, 2, 3, 4, 5, ])
    vector_d = Vector([6, 7, 8, 9, 10, ])
    assert vector_c + vector_d == [7, 9, 11, 13, 15, ]
    assert vector_c - vector_d == [-5, -5, -5, -5, -5, ]
    assert vector_c * vector_d == 130
    assert (vector_c * vector_d) / (vector_c.length * vector_d.length) == 0.9649505047327671
    assert vector_c.length == 7.416198487095663
    assert vector_d.length == 18.16590212458495
