from lab_02.task_03 import Vector
import unittest

class TestTask3(unittest.TestCase):

    def test_vector_sum(self):
        vector_a = Vector(vector_values_list=[1, 2, 3, 4, 5])
        vector_b = Vector(vector_values_list=[6, 7, 8, 9, 10])
        self.assertEqual((vector_a+vector_b), [7, 9, 11, 13, 15])

    def test_vector_residual(self):
        vector_a = Vector(vector_values_list=[1, 2, 3, 4, 5])
        vector_b = Vector(vector_values_list=[6, 7, 8, 9, 10])
        self.assertEqual((vector_a-vector_b), [-5, -5, -5, -5, -5])

    def test_vector_multiplication(self):
        vector_a = Vector(vector_values_list=[1, 2, 3, 4, 5])
        vector_b = Vector(vector_values_list=[6, 7, 8, 9, 10])
        self.assertEqual((vector_a * vector_b), 130)

    def test_vector_a_long(self):
        vector_a = Vector(vector_values_list=[1, 2, 3, 4, 5])
        self.assertEqual(vector_a.length, 7.416198487095663)
    def test_vector_b_long(self):
        vector_b = Vector(vector_values_list=[6, 7, 8, 9, 10])
        self.assertEqual(vector_b.length, 18.16590212458495)

    def test_vector_cos(self):
        vector_a = Vector(vector_values_list=[1, 2, 3, 4, 5])
        vector_b = Vector(vector_values_list=[6, 7, 8, 9, 10])
        self.assertEqual(((vector_a * vector_b) / (vector_a.length * vector_b.length)),0.9649505047327671)


