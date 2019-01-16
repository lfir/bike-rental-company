import unittest
from datetime import timedelta
from bike_rental.weekly import WeeklyRental
from bike_rental.daily import DailyRental
from bike_rental.hourly import HourlyRental


class TestClient(unittest.TestCase):

    def setUp(self):
        self.hourly_rental = HourlyRental(5)
        self.daily_rental = DailyRental(4)
        self.weekly_rental = WeeklyRental(3)

    def test_initial_attrs(self):
        self.assertEqual(self.hourly_rental.price, 25)
        self.assertEqual(self.daily_rental.price, 80)
        self.assertEqual(self.weekly_rental.price, 180)

    def test_correct_unit_prices(self):
        self.assertEqual(HourlyRental.unit_price(), 5)
        self.assertEqual(DailyRental.unit_price(), 20)
        self.assertEqual(WeeklyRental.unit_price(), 60)

    def test_correct_rental_duration(self):
        self.assertEqual(self.hourly_rental._end - timedelta(hours=5),
                         self.hourly_rental._start)
        self.assertEqual(self.daily_rental._end - timedelta(days=4),
                         self.daily_rental._start)
        self.assertEqual(self.weekly_rental._end - timedelta(weeks=3),
                         self.weekly_rental._start)
