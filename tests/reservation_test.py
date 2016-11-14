import unittest
from reservation import Reservation
from flight import Flight
from passanger import Passanger


class TestDateClass(unittest.TestCase):
    """docstring for TestFlightClass"""

    def setUp(self):
        self.reservation = Reservation(
            Flight(None, None, None, None, None, None, None, None),
            Passanger(None, None, None, None), False)

    def test_model_attribute_values(self):
        self.assertTrue(isinstance(self.reservation.flight, Flight))
        self.assertTrue(isinstance(self.reservation.passenger, Passanger))
        self.assertEqual(self.reservation.accepted, False)


if __name__ == '__main__':
    unittest.main()
