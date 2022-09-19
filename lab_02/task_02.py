'''Задание 2 (1 балл): Опишите класс комплексных чисел. У пользователя должна быть возможность
 создать его объект на основе числа и в алгебраической форме, и в полярной. Класс должен
 поддерживать основные математические операции (+, -, *, /) за счет перегрузки соответствующих
  магических методов. Также он должен поддерживать возможность получить число в алгебраической
 и полярной форме. Допускается использование модуля math.'''

import math


# Класс получает значение и реализует преобразования как из алгебраической записи в полярную, так и обратно

class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a  # Действительная часть
        self.b = b  # Мнимая часть

    @staticmethod
    def alg_polar(a: float, b: float) -> float:
        """

            метод принимает комплексное число и преобразовывает
            число из алгебраической формы в полярную.
        """
        a = math.sqrt(a ** 2 + b ** 2)
        b = math.atan(b / a)

        return a, b

    @staticmethod
    def polar_alg(a: float, b: float) -> float:
        """

            метод принимает комплексное число и преобразовывает
            из полярной в алгебраическую форму
        """
        a = a * math.cos(b)
        b = a * math.sin(b)

        return a, b

    """

        Перезагрузка операторов вычислений
    """

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b, self.a * self.b + other.b * self.a)

    def __truediv__(self, other):
        return complex(self.a / other.a, self.b / other.b)


if __name__ == "__main__":
    print('----------Ввод в алгебраической форме------------------------')
    one_number = ComplexNumber(3.7, 4.5)
    two_number = ComplexNumber(2, 3.4)

    print('---------Расчет в алгебраической форме------------------------------')

    print('Сумма', one_number + two_number)
    assert ComplexNumber(3.7, 4.5) + ComplexNumber(2, 3.4) == (5.7 + 7.9j)
    print('Разность', one_number - two_number)
    assert ComplexNumber(3.7, 4.5) - ComplexNumber(2, 3.4), (1.7000000000000002 + 1.1j)
    print('Произведение', one_number * two_number)
    assert ComplexNumber(3.7, 4.5) * ComplexNumber(2, 3.4) == (-7.899999999999999 + 29.230000000000004j)
    print('Частное', one_number / two_number)
    assert ComplexNumber(3.7, 4.5) / ComplexNumber(2, 3.4) == (1.85 + 1.3235294117647058j)

    print('---------Преобразование в полярную форму и расчет-----------------------')

    polar_a, polar_b = ComplexNumber.alg_polar(3.7, 4.5)
    polar_c, polar_d = ComplexNumber.alg_polar(2, 3.4)
    p_one_number = ComplexNumber(polar_a, polar_b)
    p_two_number = ComplexNumber(polar_c, polar_d)
    print('T', p_one_number + p_two_number)
    print(p_one_number - p_two_number)
    print(p_one_number * p_two_number)
    print(p_one_number / p_two_number)
    print()
    print('---------При вводе данных в полярной форме------------------------------')
    print()
    print('---------Расчет в полярной форме------------------------------')
    one_number = ComplexNumber(2.1232, 4.3234)

    two_number = ComplexNumber(-0.8423, 1.9232)
    print(one_number + two_number)
    assert ComplexNumber(2.1232, 4.3234) + ComplexNumber(-0.8423, 1.9232) == (1.2809000000000001 + 6.246600000000001j)
    print(one_number - two_number)
    assert ComplexNumber(2.1232, 4.3234) - ComplexNumber(-0.8423, 1.9232) == (2.9655000000000005 + 2.4002000000000003j)
    print(one_number * two_number)
    assert ComplexNumber(2.1232, 4.3234) * ComplexNumber(-0.8423, 1.9232) == (-10.10313424 + 13.262781120000003j)
    print(one_number / two_number)
    assert ComplexNumber(2.1232, 4.3234) / ComplexNumber(-0.8423, 1.9232) == (-2.5207170841742848 + 2.248024126455907j)
    print()
    print('---------Преобразование в алгебраическую форму и расчет-----------------------')
    print()
    polar_a, polar_b = ComplexNumber.polar_alg(2.1, 4.3)
    polar_c, polar_d = ComplexNumber.polar_alg(-0.84, 1.92)

    p_one_number = ComplexNumber(polar_a, polar_b)
    p_two_number = ComplexNumber(polar_c, polar_d)

    print(p_one_number + p_two_number)
    print(p_one_number - p_two_number)
    print(p_one_number * p_two_number)
    print(p_one_number / p_two_number)
