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

    #pylint: disable=too-many-arguments
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

    #pylint: disable=line-too-long
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
        """
        Static method that returns the instance of the Plate class.

        Returns
        -------
        Plate
            The instance of the Plate class.
        """
        if Plate.instance is None:
            Plate.instance = Plate()
        return Plate.instance

    def __str__(self):
        attrs = self.__dict__
        attribute_str = ', '.join([f"{key.replace('_Plate__', '')}: {value}" for key, value in attrs.items()])
        return f"{self.__class__.__name__}({attribute_str})"

    @property
    def diameter(self):
        """
        Getter method for the diameter of the plate.

        Returns
        -------
        int or float
            The diameter of the plate.
        """
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        """
        Setter method for the diameter of the plate.

        Parameters
        ----------
        diameter : int or float
            The new diameter value for the plate.

        Returns
        -------
        None
        """
        self.__diameter = diameter

    @property
    def material(self):
        """
        Getter method for the material of the plate.

        Returns
        -------
        str
            The material of the plate.
        """
        return self.__material

    @material.setter
    def material(self, material):
        """
        Setter method for the material of the plate.

        Parameters
        ----------
        material : str
            The new material value for the plate.

        Returns
        -------
        None
        """
        self.__material = material

    @property
    def color(self):
        """
        Getter method for the color of the plate.

        Returns
        -------
        str
            The color of the plate.
        """
        return self.__color

    @color.setter
    def color(self, color):
        """
        Setter method for the color of the plate.

        Parameters
        ----------
        color : str
            The new color value for the plate.

        Returns
        -------
        None
        """
        self.__color = color

    @property
    def is_clean(self):
        """
        Getter method for the cleanliness status of the plate.

        Returns
        -------
        bool
            The cleanliness status of the plate.
        """
        return self.__is_clean

    @is_clean.setter
    def is_clean(self, is_clean):
        """
        Setter method for the cleanliness status of the plate.

        Parameters
        ----------
        is_clean : bool
            The new cleanliness status for the plate.

        Returns
        -------
        None
        """
        self.__is_clean = is_clean

    @property
    def has_food(self):
        """
        Getter method for the food status of the plate.

        Returns
        -------
        bool
            The food status of the plate.
        """
        return self.__has_food

    @has_food.setter
    def has_food(self, has_food):
        """
        Setter method for the food status of the plate.

        Parameters
        ----------
        has_food : bool
            The new food status for the plate.

        Returns
        -------
        None
        """
        self.__has_food = has_food
