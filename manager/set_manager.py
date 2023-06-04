"""
Module: set_manager.py
This module defines the class SetManager.
"""
from manager.plate_manager import PlateManager


class SetManager:
    """
    A class to represent a set manager.

    Attributes
    ----------
    manager : PlateManager
        The instance of PlateManager containing the plates.
    current_index : int
        The current index for iterating over the plates.

    Methods
    -------
    __init__(plate_manager: PlateManager)
        Initializes a new instance of SetManager.
    __iter__()
        Returns an iterator over the food items in the plates.
    __len__()
        Returns the total number of food items in the plates.
    __getitem__(index: int)
        Returns the food set of the plate at the given index.
    __next__()
        Returns the next food set in the iteration.
    """
    def __init__(self, plate_manager: PlateManager):
        self.manager = plate_manager
        self.current_index = 0

    def __iter__(self):
        self.current_index = 0
        return self

    def __len__(self):
        length = 0
        for plate in self.manager:
            length += len(plate.food_set)
        return length

    def __getitem__(self, index):
        return self.manager[index].food_set

    def __next__(self):
        if self.current_index >= len(self.manager):
            raise StopIteration
        food_set = self.manager[self.current_index].food_set
        self.current_index += 1
        return food_set
