import unittest
from airline import Airline


class TestDateClass(unittest.TestCase):
    """docstring for TestFlightClass"""

    def setUp(self):
        self.airline = Airline("HackBulgaria-Airline")

    def test_model_attribute_values(self):
        self.assertEqual(self.airline.name, "HackBulgaria-Airline")


if __name__ == '__main__':
    unittest.main()
