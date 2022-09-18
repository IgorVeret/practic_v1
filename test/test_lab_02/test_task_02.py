from lab_02.task_02 import ComplexNumber
import unittest


class TestTask2(unittest.TestCase):

    # Расчет в алгебраической форме
    def test_complex_alg_sum(self):
        self.assertEqual(ComplexNumber(3.7, 4.5) + ComplexNumber(2, 3.4), (5.7 + 7.9j))

    def test_complex_alg_residual(self):
        self.assertEqual(ComplexNumber(3.7, 4.5) - ComplexNumber(2, 3.4), (1.7000000000000002 + 1.1j))

    def test_complex_alg_multiplication(self):
        self.assertEqual(ComplexNumber(3.7, 4.5) * ComplexNumber(2, 3.4), (-7.899999999999999 + 29.230000000000004j))

    def test_complex_alg_division(self):
        self.assertEqual(ComplexNumber(3.7, 4.5) / ComplexNumber(2, 3.4), (1.85 + 1.3235294117647058j))

    # Преобразование из алгебраической в полярную форму и расчет
    def test_complex_alg_mod_polar(self):
        self.assertEqual(ComplexNumber.alg_polar(3.7, 4.5), (5.825804665451804, 0.6576996192712858))

    # Преобразование из полярной в алгебраическую форму и расчет
    def test_complex_polar_alg(self):
        self.assertEqual(ComplexNumber.polar_alg(2.1, 4.3), (-0.8416782613679484, 0.771116952767819))

    # Расчет в полярной форме
    def test_complex_pol_sum(self):
        self.assertEqual(ComplexNumber(2.1232, 4.3234) + ComplexNumber(-0.8423, 1.9232),
                         (1.2809000000000001 + 6.246600000000001j))

    def test_complex_pol_residual(self):
        self.assertEqual(ComplexNumber(2.1232, 4.3234) - ComplexNumber(-0.8423, 1.9232),
                         (2.9655000000000005 + 2.4002000000000003j))

    def test_complex_pol_multiplication(self):
        self.assertEqual(ComplexNumber(2.1232, 4.3234) * ComplexNumber(-0.8423, 1.9232),
                         (-10.10313424 + 13.262781120000003j))

    def test_complex_pol_division(self):
        self.assertEqual(ComplexNumber(2.1232, 4.3234) / ComplexNumber(-0.8423, 1.9232),
                         (-2.5207170841742848 + 2.248024126455907j))

