from lab_02.task_04 import func
import unittest


class TestTask4(unittest.TestCase):

    def test_decorator(self):
        self.assertEqual(func(1), None)
