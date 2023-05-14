class Plate:
    instance = None

    def __init__ (self, diameter = None, material = None, color = None, is_clean = False, has_food = False):
        self.__diameter = diameter
        self.__material = material
        self.__color = color
        self.__is_clean = is_clean
        self.__has_food = has_food

    def wash(self):
        self.__is_clean = True

    def dirty(self):
        self.__is_clean = False

    def eat(self):
        self.__has_food = False
        self.dirty()

    def add_food(self):
        self.__has_food = True

    @staticmethod
    def get_instance():
        if Plate.instance is None:
            Plate.instance = Plate()
        return Plate.instance

    def __str__ (self):
        return f"Plate: diameter = {self.__diameter}, material = {self.__material}, " \
               f"color = {self.__color}, is_clean = {self.__is_clean}, has_food = {self.__has_food},"

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

plates = [Plate(12.3, "ceramic", "red", True, True),
          Plate(),
          Plate.get_instance(),
          Plate.get_instance()]

for plate in plates:
    print(plate)
