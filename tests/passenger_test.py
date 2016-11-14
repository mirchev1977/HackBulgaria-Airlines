import unittest
from passanger import Passanger
from flight import Flight


class TestDateClass(unittest.TestCase):
    """docstring for TestFlightClass"""

    def setUp(self):
        self.passenger = Passanger(
            first_name="Rositsa", last_name="Zlateva", flight=Flight(
                None, None, None, None, None, None, None, None), age=22)

    def test_model_attribute_values(self):
        self.assertEqual(self.passenger.first_name, "Rositsa")
        self.assertEqual(self.passenger.last_name, "Zlateva")
        self.assertEqual(self.passenger.age, 22)
        self.assertTrue(isinstance(self.passenger.flight, Flight))


if __name__ == '__main__':
    unittest.main()
