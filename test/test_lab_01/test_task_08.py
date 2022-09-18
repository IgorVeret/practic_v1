from lab_01.task_08 import task
import unittest


class TestTask8(unittest.TestCase):

    def test_func(self):
        lst = [(233, 465, 67, 85), (32, 54, 656, 87), (2, 5, 7, 89), (1, 3, 45, 6)]
        result= [465, 233, 85, 67, 656, 87, 54, 32, 89, 7, 5, 2, 45, 6, 3, 1]
        self.assertEqual(task(lst), result)
