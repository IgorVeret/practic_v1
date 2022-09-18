from lab_01.task_09 import task_09_func
import unittest


class TestTask9(unittest.TestCase):

    def test_func(self):
        result = [1, 5]
        self.assertEqual(task_09_func([5]), result)

    def test_func1(self):
        result = [1, 10]
        self.assertEqual(task_09_func([10]), result)
