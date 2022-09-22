from task_03_03 import task_3
import unittest


class TestTask3(unittest.TestCase):

    def test_empty(self):

        self.assertEqual(task_3([ ], [ ]), [ ])


if __name__ == "__main__":
    TestTask3()
