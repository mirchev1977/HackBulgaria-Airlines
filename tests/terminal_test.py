import unittest
from terminal import Terminal


class TestDateClass(unittest.TestCase):
    """docstring for TestFlightClass"""

    def setUp(self):
        self.terminal = Terminal(number=25, max_flights=35)

    def test_model_attribute_values(self):
        self.assertEqual(self.terminal.number, 25)
        self.assertEqual(self.terminal.max_flights, 35)


if __name__ == '__main__':
    unittest.main()
