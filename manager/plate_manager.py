"""
Module: plate_manager.py
This module defines the abstract class PlateManager.
"""
from models.plate import Plate


class PlateManager:
    """
    A class to represent a plate manager.
    ...
    Attributes
    ----------
    plate_list : list
        list with plates

    Methods
    -------
    add_plate():
        adding plate in list
    find_plate_with_diameter_greater_than():
        return list plate with diameter greater than input.
    find_all_clean():
        return list all clean plates.
    """
    plate_list = []

    def add_plate(self, plate: Plate):
        """
        add plate in list.

        Parameters
        ----------
        Plate

        Return
        ----------
        None
        """
        self.plate_list.append(plate)

    def find_plate_with_diameter_greater_than(self, value: float):
        """
        return list plate with diameter greater than input.

        Parameters
        ----------
        float

        Return
        ----------
        list
        """
        print('All plates with diameter greater than {value}cm:')
        filtered_plates = [plate for plate in self.plate_list if plate.diameter > value]
        for plate in filtered_plates:
            print(plate)

    def find_all_clean(self):
        """
        return list all clean plates.

        Parameters
        ----------
        None

        Return
        ----------
        list
        """
        print('All clean')
        filtered_plates = [plate for plate in self.plate_list if plate.is_clean]
        for plate in filtered_plates:
            print(plate)
