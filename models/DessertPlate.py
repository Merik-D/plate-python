import math
from models.Plate import Plate


class DessertPlate(Plate):

    def __init__(self, diameter, material, color, is_clean, has_food, picture, sections):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.__picture = picture
        self.__sections = sections

    def get_max_food_weight(self):
        return math.pi * self.diameter ** 3 / 24

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join(
            [f"{key.replace('_Plate__', '').replace('_DessertPlate__', '')}: {value}" for key, value in attrs.items()])
        return f"{self.__class__.__name__}({attribute_str})"
