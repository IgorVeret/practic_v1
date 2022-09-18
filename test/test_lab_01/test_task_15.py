from lab_01.task_15 import task_15_func1, task_15_func2
import unittest


class TestTask15(unittest.TestCase):

    def test_func_one(self):
        n = 'In Google Chrome the address bar  that sits at the top of the browser  window'
        result = ['73n 7', 'oogle 67hrome the address bar  that sits at the top of the browser  window']
        self.assertEqual(task_15_func1(n), result)

    def test_func_two(self):
        n = 'In Google Chrome the address bar  that sits at the top of the browser  window'
        result = ['73n 7', 'oogle 67hrome the address bar  that sits at the top of the browser  window']
        self.assertEqual(task_15_func2(n), result)
