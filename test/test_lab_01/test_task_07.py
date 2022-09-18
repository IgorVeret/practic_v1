from lab_01.task_07 import task_07_func_1, task_07_func_2, task_07_func_3
import unittest


class TestTask7(unittest.TestCase):

    def test_func_one(self):
        lst = [1, 4, 2, -3, 6, 7, 8, 9]
        result = [81, 64, 49, 36, 16, 4, 1]
        self.assertEqual(task_07_func_1(lst), result)

    def test_func_two(self):
        lst = [1, 4, 2, -3, 6, 7, 8, 9]
        result = [81, 64, 49, 36, 16, 4, 1]
        self.assertEqual(task_07_func_2(lst), result)

    def test_func_three(self):
        lst = [1, 4, 2, -3, 6, 7, 8, 9]
        result = [81, 64, 49, 36, 16, 4, 1]
        self.assertEqual(task_07_func_3(lst), result)

