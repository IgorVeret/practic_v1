from lab_01.task_03 import task_03_func
import unittest


class TestTask3(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(task_03_func(5), 153)
