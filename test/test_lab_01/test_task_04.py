from lab_01.task_04 import task_04_func1, task_04_func2, task_04_func3
import unittest


class TestTask4(unittest.TestCase):

    def test_func1_palindrome(self):
        self.assertEqual(task_04_func1("qwerewq"), 'Палиндром')

    def test_func2_palindrome(self):
        self.assertEqual(task_04_func2("qwerewq"), 'Палиндром')

    def test_func3_palindrome(self):
        self.assertEqual(task_04_func3("qwerewq"), 'Палиндром')

    def test_func1_no_palindrome(self):
        self.assertEqual(task_04_func1("qweeerewq"), 'Не палиндром')

    def test_func2_no_palindrome(self):
        self.assertEqual(task_04_func2("qweeerewq"), 'Не палиндром')

    def test_func3_no_palindrome(self):
        self.assertEqual(task_04_func3("qweeerewq"), 'Не палиндром')
