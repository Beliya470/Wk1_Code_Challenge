import unittest
from code_challenge import to_24_hour, two_are_positive, solve

class TestCodeChallenge(unittest.TestCase):

    def test_to_24_hour(self):
        self.assertEqual(to_24_hour(8, 30, "am"), "0830")
        self.assertEqual(to_24_hour(8, 30, "pm"), "2030")
        self.assertEqual(to_24_hour(12, 0, "am"), "0000")

    def test_two_are_positive(self):
        self.assertTrue(two_are_positive(2, 4, -3))
        self.assertTrue(two_are_positive(-4, 6, 8))
        self.assertTrue(two_are_positive(4, -6, 9))
        self.assertFalse(two_are_positive(-4, 6, 0))
        self.assertFalse(two_are_positive(4, 6, 10))
        self.assertFalse(two_are_positive(-14, -3, -4))

    def test_solve(self):
        self.assertEqual(solve("zodiacs"), 26)
        self.assertEqual(solve("strength"), 57)

if __name__ == '__main__':
    unittest.main()
