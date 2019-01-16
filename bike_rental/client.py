"""This is the client module.
Provides the Client abstract class.
"""
from abc import ABC, abstractmethod


class Client(ABC):
    """ABC that defines the minimum interface needed for concrete
    clients to collaborate with the rental system.
    """
    __rentals = None
    __balance = None

    @abstractmethod
    def request(self, rentals):
        """Request one or more rentals to the rental system. To
        be implemented by subclasses.
        """
