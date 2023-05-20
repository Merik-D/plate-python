import math
from models.Plate import Plate


class PicnicPlate(Plate):

    def __init__(self, diameter, material, color, is_clean, has_food, lid, compartments):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.__lid = lid
        self.__compartments = compartments

    def get_max_food_weight(self):
        return math.pi * self.diameter ** 3 / 16

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join(
            [f"{key.replace('_Plate__', '').replace('_PicnicPlate__', '')}: {value}" for key, value in attrs.items()])
        return f"{self.__class__.__name__}({attribute_str})"
