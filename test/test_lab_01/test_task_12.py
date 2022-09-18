from lab_01.task_12 import task_12_func
import unittest.mock


class TestTask12(unittest.TestCase):
    @unittest.mock.patch('task_12.task_12_func')
    def test_func_one(self, mocked):
        self.assertFalse(mocked.called)
if __name__ == "__main__":
    TestTask12()
