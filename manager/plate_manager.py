"""
Module: plate_manager.py
This module defines the class PlateManager.
"""
from decorators.call_history import call_history
from decorators.enforce_snake_case import enforce_snake_case
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

    def __len__(self):
        return len(self.plate_list)

    def __getitem__(self, index):
        return self.plate_list[index]

    def __iter__(self):
        return iter(self.plate_list)

    @enforce_snake_case
    def get_max_food_weight_list(self):
        """
        Return a list of maximum food weights for all plates.

        Returns
        -------
        list
            List of maximum food weights for all plates.
        """
        return [plate.get_max_food_weight() for plate in self.plate_list]

    @call_history
    def plate_enumerate(self):
        """
        Print the concatenation of each object with its index in the list.

        Returns
        -------
        None
        """
        print('\n'.join([f'{index + 1}) {obj}' for index, obj in enumerate(self.plate_list)]))

    def plate_zip(self):
        """
        Return a string representation of plates with their maximum food weights.

        Returns
        -------
        str
            String representation of plates with their maximum food weights.
        """
        results = self.get_max_food_weight_list()
        # pylint: disable=line-too-long
        return '\n'.join([f'{obj}", max food weight:" {result}' for obj, result in zip(self.plate_list, results)])

    def check_conditions(self, condition):
        """
        Check if the given condition is satisfied for all or any plates.

        Parameters
        ----------
        condition : function
            The condition to check for each plate.

        Returns
        -------
        dict
            A dictionary containing the results for 'all' and 'any' conditions.
        """
        result = {
            'all': all(condition(obj) for obj in self.plate_list),
            'any': any(condition(obj) for obj in self.plate_list)
        }
        return result
