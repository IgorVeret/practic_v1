from lab_01.task_16 import task_16_func
import unittest


class TestTask16(unittest.TestCase):

    def test_phone_number(self):
        n = 'ewew+79536761226zx rewqrewew +79536761227d hddsfewew +7(953)6761229 rrwe ss \
        8 953 676 1230 fgfs +7(953)676-12-31'
        result = ['+79536761226', '+79536761227', '+7(953)6761229', '8 953 676 1230', '+7(953)676-12-31']
        self.assertEqual(task_16_func(n), result)

    def test_epmty_list(self):
        n = 'ewew rewqrewew  hddsfewew  rrwe ss  fgfs '
        result = []
        self.assertEqual(task_16_func(n), result)
