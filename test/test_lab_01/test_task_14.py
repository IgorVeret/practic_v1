from lab_01.task_14 import task_14_func
import unittest


class TestTask14(unittest.TestCase):

    def test_func_int(self):
        result = ['__abs__', '__add__', '__and__']
        self.assertEqual(task_14_func(5), result)

    def test_func_str(self):
        result = ['__setattr__', '__sizeof__', '__str__', '__subclasshook__']
        self.assertEqual(task_14_func("str"), result)

    def test_func_three(self):
        result = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
        self.assertEqual(task_14_func([1, 2]), result)
