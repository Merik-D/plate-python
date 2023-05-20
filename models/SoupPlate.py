import math
from models.Plate import Plate


class SoupPlate(Plate):

    def __init__(self, diameter, material, color, is_clean, has_food, plate_depth_in_cm, type_of_soup):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.__plate_depth_in_cm = plate_depth_in_cm
        self.__type_of_soup = type_of_soup

    def get_max_food_weight(self):
        return math.pi * self.plate_depth_in_cm * self.diameter ** 2 / 16

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join(
            [f"{key.replace('_Plate__', '').replace('_SoupPlate__', '')}: {value}" for key, value in attrs.items()])
        return f"{self.__class__.__name__}({attribute_str})"

    @property
    def plate_depth_in_cm(self):
        return self.__plate_depth_in_cm
