from task_05_03 import preprocess, task_5
import unittest


class TestTask5(unittest.TestCase):

    def test_preprocess_reg(self):
        text = '>so, if he s Feeling lucky, your Runner at second Can Sprint for gloryn >as soon as the ball ' \
               'is popped up.  if it isn t caught, he s probably scored    >a run.  if it is, hes probably headed' \
               ' for aaa.'
        result = ['so', 'if', 'he', 's', 'feeling', 'lucky', 'your', 'runner', 'at', 'second', 'can', 'sprint',
                  'for', 'gloryn', 'as', 'soon', 'as', 'the', 'ball', 'is', 'popped', 'up', 'if', 'it', 'isn', 't',
                  'caught', 'he', 's', 'probably', 'scored', 'a', 'run', 'if', 'it', 'is', 'hes', 'probably', 'headed',
                  'for', 'aaa']
        self.assertEqual(preprocess(text), result)


if __name__ == "__main__":
    TestTask5()
