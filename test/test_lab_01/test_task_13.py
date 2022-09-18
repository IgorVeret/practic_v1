from lab_01.task_13 import test, task_13_func
import unittest


class TestTask13(unittest.TestCase):

    def test_func(self):
        result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(test(10), result)

    def test_not_in_range(self):
        self.assertEqual(test(-2), [])

