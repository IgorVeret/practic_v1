from lab_01.task_05 import task_05_func, task_05_func_1
import unittest


class TestTask5(unittest.TestCase):

    def test_var1_Dictionary(self):
        text = 'в виде строки напишите функцию которая Возвращает Словарь словарь'
        result = {'в': 1, 'виде': 1, 'возвращает': 1, 'которая': 1, 'напишите': 1, 'словарь': 2, 'строки': 1,
                  'функцию': 1}
        self.assertEqual(task_05_func(text), result)

    def test_var2_Dictionary(self):
        text = 'в виде строки напишите функцию которая Возвращает Словарь словарь'
        result = {'в': 1, 'виде': 1, 'возвращает': 1, 'которая': 1, 'напишите': 1, 'словарь': 2, 'строки': 1,
                  'функцию': 1}
        self.assertEqual(task_05_func_1(text), result)
