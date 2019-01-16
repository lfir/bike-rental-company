"""This is the daily module.
Provides the DailyRental class.
"""
from bike_rental.rental import Rental
from datetime import datetime, timedelta


class DailyRental(Rental):
    """Subclass of the Rental class that represents
    a daily rental.
    """
    @property
    def price(self):
        """:return: int"""
        return self._price

    def __init__(self, days):
        """Set attributes of a new DailyRental object.
        :param days: int
        """
        self._price = self.unit_price() * days
        self._start = datetime.now()
        self._end = self._start + timedelta(days=days)

    @staticmethod
    def unit_price():
        """Return the price of a one day rental.
        :return: int"""
        return 20
