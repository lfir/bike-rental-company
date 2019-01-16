"""This is the family_rental module.
Provides the FamilyRental class.
"""
from bike_rental.promotion import Promotion


class FamilyRental(Promotion):
    """Subclass of the Promotion class. Represents
    the Family Rental promotion.
    """

    def valid_conditions(self, rentals):
        """Return whether rentals contains between 3 and 5 objects,
        including endpoints.
        :param rentals: tuple with one or more Rental objects
        :return: bool
        """
        return len(rentals) in range(3, 6)

    def apply_discount(self, rentals):
        """If the conditions for this promotion are met, apply a
        30% discount to the total price of the rentals.
        Return the total.
        :param rentals: tuple with one or more Rental objects
        :return: float
        """
        total_price = 0
        for rental in rentals:
            total_price += rental.price

        if self.valid_conditions(rentals):
            total_price *= 0.7

        return total_price
