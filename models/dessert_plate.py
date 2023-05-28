"""
Module: dessert_plate.py
This module defines the class DessertPlate.
"""
import math
from models.plate import Plate

# pylint: disable=too-few-public-methods
class DessertPlate(Plate):
    """
    A class to represent a dessert plate.
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
    picture: bool
        is there a picture.
    sections : int
        number of sections in the plate.
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
    get_max_food_weight():
        return max food weight
    """
    # pylint: disable=too-many-arguments
    def __init__(self, diameter, material, color, is_clean, has_food, picture, sections):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.picture = picture
        self.sections = sections

    def get_max_food_weight(self):
        """
        return max food weight.

        Parameters
        ----------
        None

        Return
        ----------
        float
        """
        return math.pi * self.diameter ** 3 / 24
