"""This is the rental module.
Provides the Rental base class.
"""
from abc import ABC, abstractmethod


class Rental(ABC):
    """ABC that defines the minimum interface needed for concrete
    rental subclasses to collaborate with the rental system.
    """
    __price = None
    __start = None
    __end = None

    @staticmethod
    @abstractmethod
    def unit_price():
        """To be implemented by subclasses."""
