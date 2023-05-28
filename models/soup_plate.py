"""
Module: soup_plate.py
This module defines the class SoupPlate.
"""
import math
from models.plate import Plate


# pylint: disable=too-few-public-methods
class SoupPlate(Plate):
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
    plate_depth_in_cm : float
        depth of the plate in centimeters.
    type_of_soup : str
        type of soup served in the plate.
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
    # pylint: disable=line-too-long
    def __init__(self, diameter, material, color, is_clean, has_food, food_set, plate_depth_in_cm, type_of_soup):
        """
        :param diameter:
        :param material:
        :param color:
        :param is_clean:
        :param has_food:
        :param plate_depth_in_cm:
        :param type_of_soup:
        """
        super().__init__(diameter, material, color, is_clean, has_food, food_set={"soup", "stew"})
        self.plate_depth_in_cm = plate_depth_in_cm
        self.type_of_soup = type_of_soup

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
        return math.pi * self.plate_depth_in_cm * (self.diameter ** 2) / 16
