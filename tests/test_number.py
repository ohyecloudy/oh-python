import unittest

class TestNumberMethods(unittest.TestCase):

    def test_power_operator(self):
        self.assertEqual(5 ** 2, 25)

if __name__ == '__main__':
    unittest.main()
