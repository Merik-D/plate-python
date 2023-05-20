import math
from models.Plate import Plate


class SaladPlate(Plate):

    def __init__(self, diameter, material, color, is_clean, has_food, shape, dishwasher_safe):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.__shape = shape
        self.__dishwasher_safe = dishwasher_safe

    def get_max_food_weight(self):
        return math.pi * self.diameter ** 3 / 24

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join(
            [f"{key.replace('_Plate__', '').replace('_SaladPlate__', '')}: {value}" for key, value in attrs.items()])
        return f"{self.__class__.__name__}({attribute_str})"
