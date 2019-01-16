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
        return self.__price

    def __init__(self, days):
        """Set attributes of a new DailyRental object.
        :param days: int
        """
        self.__price = self.unit_price() * days
        self.__start = datetime.now()
        self.__end = self.__start + timedelta(days=days)

    @staticmethod
    def unit_price():
        """Return the price of a one day rental.
        :return: int"""
        return 20
