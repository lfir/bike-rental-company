import unittest
from bike_rental.bike_rental_client import BikeRentalClient
from bike_rental.bike_rental_store import BikeRentalStore
from bike_rental.family_rental import FamilyRental
from bike_rental.weekly import WeeklyRental


class TestClient(unittest.TestCase):

    def setUp(self):
        self.store = BikeRentalStore(FamilyRental())
        self.client = BikeRentalClient(self.store)
        self.rentals = (WeeklyRental(1), WeeklyRental(3))

    def test_initial_attrs(self):
        self.assertEqual(self.client.rentals, [])
        self.assertEqual(self.client.balance, 0.0)

    def test_request_increments_balance(self):
        self.client.request(self.rentals)

        self.assertEqual(self.client.balance, WeeklyRental.unit_price() * 4)

    def test_request_registers_rentals(self):
        self.client.request(self.rentals)

        self.assertTrue(self.rentals[0] in self.client.rentals)
        self.assertTrue(self.rentals[1] in self.client.rentals)
