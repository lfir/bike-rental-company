"""This is the bike_rental_client module.
Provides the BikeRentalClient class.
"""
from bike_rental.client import Client


class BikeRentalClient(Client):
    """Subclass of the Client class that represents customers of the
    bike rental company/store.
    """
    _store = None

    @property
    def rentals(self):
        """Return a list of rentals made by this client.
        :return: list
        """
        return self._rentals

    @property
    def balance(self):
        """Return the total cost of this client's rentals.
        :return: float
        """
        return self._balance

    def __init__(self, store):
        """Set attributes of a new BikeRentalClient object.
        :param store: BikeRentalStore
        """
        self._rentals = []
        self._balance = 0.0
        self._store = store

    def request(self, rentals):
        """Override method in Client. Request rentals to the bike
        rental system and register the cost and rentals of the
        operation.
        :param rentals: tuple with one or more Rental objects
        """
        cost = self._store.handle_request(self, rentals)
        self._balance += cost
        for rental in rentals:
            self._rentals.append(rental)
