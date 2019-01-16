import unittest
from bike_rental.bike_rental_client import BikeRentalClient
from bike_rental.bike_rental_store import BikeRentalStore
from bike_rental.family_rental import FamilyRental
from bike_rental.weekly import WeeklyRental


class TestStore(unittest.TestCase):

    def setUp(self):
        self.store = BikeRentalStore(FamilyRental())
        self.client = BikeRentalClient(self.store)
        self.rentals = (WeeklyRental(1), WeeklyRental(1))

    def test_order_returns_total_price(self):
        self.assertEqual(self.store.handle_request(self.client, self.rentals),
                         WeeklyRental.unit_price() * 2)
