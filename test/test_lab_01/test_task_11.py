from lab_01.task_11 import task_11_func
import unittest


class TestTask11(unittest.TestCase):

    def test_func_one(self):
        first_list = [10, 10, 23, 10, 123, 66, 78, 123, 600]
        second_list = [11, 10, 23, 10, 125, 66, 87, 123]
        result = [600, 78]
        self.assertEqual(task_11_func(first_list, second_list), result)
