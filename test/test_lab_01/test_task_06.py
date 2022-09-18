from lab_01.task_06 import task_06_func
import unittest


class TestTask6(unittest.TestCase):

    def test_func_one(self):
        input_str = 'во поле березка стояла э'
        input_char = 'э'
        result = (23, None)
        self.assertEqual(task_06_func(input_str, input_char), result)

    def test_func_two(self):
        input_str = 'во поле березка стояла э'
        input_char = 'е'
        result = (6, 11)
        self.assertEqual(task_06_func(input_str, input_char), result)

    def test_func_none(self):
        input_str = 'во поле березка стояла э'
        input_char = 'ю'
        result = (None, None)
        self.assertEqual(task_06_func(input_str, input_char), result)
