from lab_01.task_01 import task_01_func
import unittest


class TestTask1(unittest.TestCase):

    def test_leap_year(self):
        self.assertEqual(task_01_func(2000), 'YES')

    def test_year(self):
        self.assertEqual(task_01_func(2003), 'NO')

