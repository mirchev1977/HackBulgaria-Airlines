import unittest
from date import Date


class TestDateClass(unittest.TestCase):
    """docstring for TestFlightClass"""

    def setUp(self):
        self.dateTime = Date(29, 11, 2016, "15:30")

    def test_model_attribute_values(self):
        self.assertEqual(self.dateTime.date, 29)
        self.assertEqual(self.dateTime.month, 11)
        self.assertEqual(self.dateTime.year, 2016)
        self.assertEqual(self.dateTime.hour, "15:30")


if __name__ == '__main__':
    unittest.main()
