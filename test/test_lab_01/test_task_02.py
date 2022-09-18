from lab_01.task_02 import task_02_func_01, task_02_func_02
import unittest


class TestTask2(unittest.TestCase):

    def test_long1(self):
        self.assertEqual(task_02_func_01(2099), 4)

    def test_long2(self):
        self.assertEqual(task_02_func_02(5901), 4)
