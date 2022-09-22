from task_01_03 import task_1
import numpy as np
import  unittest

class TestTask1(unittest.TestCase):

    def test_arr_plus(self):
        self.assertEqual(task_1(np.array([1, 2, 3, 4, 5])), True)

    def test_arr_minus(self):
        self.assertEqual(task_1(np.array([1, -2, -3, 4, 5, 6])), False)
if __name__ == "__main__":
    TestTask1()