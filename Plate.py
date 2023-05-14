class Plate:
    """
    A class to represent a plate.
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
    """
    instance = None

    def __init__(self, diameter=None, material=None, color=None, is_clean=False, has_food=False):
        self.__diameter = diameter
        self.__material = material
        self.__color = color
        self.__is_clean = is_clean
        self.__has_food = has_food

    def wash(self):
        """
        Cleans the plate and sets the is_clean flag to True.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.__is_clean = True

    def dirty(self):
        """
        Sets the is_clean flag to False, indicating that the plate is dirty.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.__is_clean = False

    def eat(self):
        """
        Indicates that the food has been eaten, sets the has_food flag to False, and marks the plate as dirty.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.__has_food = False
        self.dirty()

    def add_food(self):
        """
        Adds food to the plate, sets the has_food flag to True.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """
        self.__has_food = True

    @staticmethod
    def get_instance():
        if Plate.instance is None:
            Plate.instance = Plate()
        return Plate.instance

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join([f"{key.replace('_Plate__', '')}: {attrs[key]}" for key in attrs])
        return f"{self.__class__.__name__}({attribute_str})"

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        self.__diameter = diameter

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def is_clean(self):
        return self.__is_clean

    @is_clean.setter
    def is_clean(self, is_clean):
        self.__is_clean = is_clean

    @property
    def has_food(self):
        return self.__has_food

    @has_food.setter
    def has_food(self, has_food):
        self.__has_food = has_food
