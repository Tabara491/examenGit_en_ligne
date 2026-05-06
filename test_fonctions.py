import unittest
from mesfonctions import addition, soustraction, multiplication, division, carre

class TestFonctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_carre(self):
        self.assertEqual(carre(3), 9)

if __name__ == "__main__":
    unittest.main()