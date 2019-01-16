"""This is the promotion module.
Provides the Promotion abstract class.
"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """ABC that defines the minimum interface needed for concrete
    promotions to collaborate with the rental system.
    """

    @abstractmethod
    def valid_conditions(self, rentals):
        """Check if this promotion applies to the given rentals. To be
        implemented by subclasses.
        """

    @abstractmethod
    def apply_discount(self, rentals):
        """Apply the corresponding discount to the cost of the rentals.
        To be implemented by subclasses.
        """
