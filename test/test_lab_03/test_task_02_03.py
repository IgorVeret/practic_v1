from task_02_03 import task_2
import numpy as np
import unittest


class TestTask2(unittest.TestCase):

    def test_arr(self):
        self.assertEqual(task_2(np.array([1, 2, 3]), 3), [1, 1, 1, 2, 2, 2, 3, 3, 3])


if __name__ == "__main__":
    TestTask2()
