"""
Module: plate.py
This module defines the abstract class Plate.
"""
from abc import ABC, abstractmethod


class Plate(ABC):
    """
    A class to represent a plate.
    ...
    Attributes
    ----------
    diameter : float
        plate diameter in centimeters.
    material : str
        material of the plate.
    color : str
        color of the plate.
    is_clean : bool
        condition of the plate (clean/dirty).
    has_food : bool
        availability of food.
    Methods
    -------
    wash():
        cleans the plate and sets the isClean flag to True.
    dirty():
        marks the plate as dirty (sets the is_clean flag to False).
    eat():
        resets the has_food flag and marks the plate as dirty.
    has_food():
        sets the has_food flag to true
    """
    instance = None

    # pylint: disable=too-many-arguments
    def __init__(self, diameter=None, material=None, color=None, is_clean=False, has_food=False):
        self.diameter = diameter
        self.material = material
        self.color = color
        self.is_clean = is_clean
        self.has_food = has_food

    def wash(self):
        """
        Cleans the plate and sets the is_clean flag to True.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.is_clean = True

    def dirty(self):
        """
        Sets the is_clean flag to False, indicating that the plate is dirty.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.is_clean = False

    # pylint: disable=line-too-long
    def eat(self):
        """
        Indicates that the food has been eaten, sets the has_food flag to False, and marks the plate as dirty.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.has_food = False
        self.dirty()

    def add_food(self):
        """
        Adds food to the plate, sets the has_food flag to True.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.has_food = True

    @staticmethod
    def get_instance():
        """
        Static method that returns the instance of the Plate class.

        Returns
        -------
        Plate
            The instance of the Plate class.
        """
        if Plate.instance is None:
            Plate.instance = Plate()
        return Plate.instance

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join([f"{key.replace('_Plate__', '')}: {value}" for key, value in attrs.items()])
        return f"Plate: {attribute_str}"

    @abstractmethod
    def get_max_food_weight(self):
        """
        abstractmethod max food weight.
        """
