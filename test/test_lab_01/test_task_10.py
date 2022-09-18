from lab_01.task_10 import task_10_func
import unittest
import os

class TestTask10(unittest.TestCase):

    def test_func(self):
        prev_extension = 'tx_'
        next_extension = 'txt'
        dir_path = os.chdir(r'dir_root')
        result=(6, 0)
        self.assertEqual(task_10_func(dir_path, prev_extension, next_extension), result)


