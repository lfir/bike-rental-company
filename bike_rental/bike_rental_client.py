"""This is the bike_rental_client module.
Provides the BikeRentalClient class.
"""
from bike_rental.client import Client


class BikeRentalClient(Client):
    """Subclass of the Client class that represents customers of the
    bike rental company/store.
    """
    __store = None

    @property
    def rentals(self):
        """Return a tuple of rentals made by this client.
        :return: tuple
        """
        return self.__rentals

    @property
    def balance(self):
        """Return the total cost of this client's rentals.
        :return: float
        """
        return self.__balance

    def __init__(self, store):
        """Set attributes of a new BikeRentalClient object.
        :param store: BikeRentalStore
        """
        self.__rentals = []
        self.__balance = 0.0
        self.__store = store

    def request(self, rentals):
        """Override method in Client. Request rentals to the bike
        rental system and register the cost and rentals of the
        operation.
        :param rentals: tuple with one or more Rental objects
        """
        cost = self.__store.handle_request(self, rentals)
        self.__balance += cost
        for rental in rentals:
            self.__rentals.append(rental)
