import unittest
from flight import Flight
from date import Date
from terminal import Terminal


class TestFlightClass(unittest.TestCase):
    """docstring for TestFlightClass"""

    def setUp(self):
        self.flight = Flight(
            start_time=Date(29, 11, 2016, hour='12:20'),
            end_time=Date(29, 11, 2016, hour='15:30'),
            passengers=100, max_passengers=120, from_dest="Sofia",
            to_dest="London", terminal=Terminal(2, 30),
            declined=False)

    def test_flight_attribute_values(self):
        self.assertEqual(self.flight.start_time.date, 29)
        self.assertEqual(self.flight.start_time.month, 11)
        self.assertEqual(self.flight.start_time.year, 2016)
        self.assertEqual(self.flight.start_time.hour, "12:20")

        self.assertEqual(self.flight.end_time.date, 29)
        self.assertEqual(self.flight.end_time.month, 11)
        self.assertEqual(self.flight.end_time.year, 2016)
        self.assertEqual(self.flight.end_time.hour, "15:30")

        self.assertEqual(self.flight.passengers, 100)
        self.assertEqual(self.flight.max_passengers, 120)

        self.assertEqual(self.flight.from_dest, "Sofia")
        self.assertEqual(self.flight.to_dest, "London")

        self.assertEqual(self.flight.terminal.number, 2)
        self.assertEqual(self.flight.terminal.max_flights, 30)

        self.assertEqual(self.flight.declined, False)



if __name__ == '__main__':
    unittest.main()
