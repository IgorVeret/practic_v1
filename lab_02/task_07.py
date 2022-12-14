'''Ставится задача расчета стоимости чашки кофе. Опишите классы нескольких типов
кофе (латте, капучино, американо), а также классы добавок к кофе
(сахар, сливки, кардамон, пенка, сироп). Используйте шаблон "декоратор".
Каждый класс должен характеризоваться методом вычисления стоимости чашки calculate_cost.
Пользователь должен иметь возможность комбинировать любое число добавок с выбранным кофе
и получить на выходе общую стоимость:
Cream(Sugar(Latte())).calculate_cost()
Первым элементом чашки всегда должен быть сам кофе, а не добавка, в противном случае при
попытке создания чашки должно выбрасываться исключение:

Cream(Latte(Sugar())).calculate_cost() -> exception
Кофе может встречаться в чашке только один раз, в противном случае при попытке создания чашки
должно выбрасываться исключение:

Cappuccino(Sugar(Latte())).calculate_cost() -> exception
Добавки могут включаться в чашку в любом количестве и порядке. Добавление новых типов кофе
и добавок не должно требовать изменения существующего кода.'''
class Calculate():
    def calculate_cost(self):
        raise Exception


class Latte(Calculate):
    def __init__(self):
        setattr(self, 'cost', 100)

    def calculate_cost(self):
        return self.cost


class Cappuccino(Calculate):
    def __init__(self):
        setattr(self, 'cost', 200)

    def calculate_cost(self):
        return self.cost


class Americano(Calculate):
    def __init__(self):
        setattr(self, 'cost', 300)

    def calculate_cost(self):
        return self.cost


# ---------------------Добавки в кофе-----------------------------------

class Sugar(Calculate):
    def __init__(self, coffee):
        self.cost = coffee.cost + 15

    def calculate_cost(self):
        return self.cost


class Cream(Calculate):
    def __init__(self, coffee):
        self.cost = coffee.cost + 20

    def calculate_cost(self):
        return self.cost


class Cardamom(Calculate):
    def __init__(self, coffee):
        self.cost = coffee.cost + 35

    def calculate_cost(self):
        return self.cost


class Foam(Calculate):
    def __init__(self, coffee):
        self.cost = coffee.cost + 40

    def calculate_cost(self):
        return self.cost


class Syrup(Calculate):
    def __init__(self, coffee):
        self.cost = coffee.cost + 45

    def calculate_cost(self):
        return self.cost

if __name__ == "__main__":
    # ----------------Введите кофе и ингридиенты-------------------------
    try:
        cup = Syrup(Syrup(Syrup(Foam(Sugar(Cardamom(Cream(Sugar(Cream(Cappuccino())))))))))

        print('Стоимость вашего заказа равна = ', cup.calculate_cost(), 'руб.')
    except NameError:
        print('Отсутствует или неправильно введен один из компонентов')
    except TypeError:
        print('Ошибка. Позиция с кофе не введена, не первая или введено\n'
              'более одного раза.')