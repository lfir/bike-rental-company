"""This is the weekly module.
Provides the WeeklyRental class.
"""
from bike_rental.rental import Rental
from datetime import datetime, timedelta


class WeeklyRental(Rental):
    """Subclass of the Rental class that represents
    a weekly rental.
    """
    @property
    def price(self):
        """:return: int"""
        return self._price

    def __init__(self, weeks):
        """Set attributes of a new WeeklyRental object.
        :param weeks: int
        """
        self._price = self.unit_price() * weeks
        self._start = datetime.now()
        self._end = self._start + timedelta(weeks=weeks)

    @staticmethod
    def unit_price():
        """Return the price of a one week rental.
        :return: int"""
        return 60
