"""
Module: picnic_plate.py
This module defines the class PicnicPlate.
"""
import math
from models.plate import Plate

# pylint: disable=too-few-public-methods
class PicnicPlate(Plate):
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
    lid : bool
        specifies if the plate has a lid.
    compartments : int
        number of compartments in the plate.
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
    def __init__(self, diameter, material, color, is_clean, has_food, food_set, lid, compartments):
        """
        :param diameter:
        :param material:
        :param color:
        :param is_clean:
        :param has_food:
        :param lid:
        :param compartments:
        """
        # pylint: disable=line-too-long
        super().__init__(diameter, material, color, is_clean, has_food, food_set={"sandwich", "fruit", "chips"})
        self.lid = lid
        self.compartments = compartments

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
        return math.pi * self.diameter ** 3 / 16
