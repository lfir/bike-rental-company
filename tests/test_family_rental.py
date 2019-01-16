import unittest
from bike_rental.family_rental import FamilyRental
from bike_rental.weekly import WeeklyRental
from bike_rental.daily import DailyRental


class TestFamilyRentalPromotion(unittest.TestCase):

    def setUp(self):
        self.promotion = FamilyRental()
        self.rentals = (WeeklyRental(5), WeeklyRental(1), WeeklyRental(2))

    def test_valid_conditions_returns_true_if_conditions_met(self):
        rentalsx4 = (WeeklyRental(5), WeeklyRental(1), WeeklyRental(2),
                     WeeklyRental(1))
        rentalsx5 = (DailyRental(5), WeeklyRental(1), DailyRental(2),
                     WeeklyRental(1), WeeklyRental(1))

        self.assertTrue(self.promotion.valid_conditions(self.rentals))
        self.assertTrue(self.promotion.valid_conditions(rentalsx4))
        self.assertTrue(self.promotion.valid_conditions(rentalsx5))

    def test_valid_conditions_returns_false_if_conditions_not_met(self):
        rentalsx2 = (WeeklyRental(5), WeeklyRental(1))
        rentalsx6 = (DailyRental(5), WeeklyRental(1), DailyRental(2),
                     WeeklyRental(1), DailyRental(2), WeeklyRental(1))

        self.assertFalse(self.promotion.valid_conditions(rentalsx2))
        self.assertFalse(self.promotion.valid_conditions(rentalsx6))

    def test_discount_applied_if_conditions_met(self):
        self.assertEqual(self.promotion.apply_discount(self.rentals),
                         WeeklyRental.unit_price() * 8 * 0.7)

    def test_discount_not_applied_if_conditions_not_met(self):
        rentalsx2 = (WeeklyRental(5), WeeklyRental(1))
        self.assertNotEqual(self.promotion.apply_discount(rentalsx2),
                            WeeklyRental.unit_price() * 6 * 0.7)
        self.assertEqual(self.promotion.apply_discount(rentalsx2),
                         WeeklyRental.unit_price() * 6)
