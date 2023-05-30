from decorators.call_history import call_history
from manager.plate_manager import PlateManager
from manager.set_manager import SetManager
from models.dessert_plate import DessertPlate
from models.picnic_plate import PicnicPlate
from models.salad_plate import SaladPlate
from models.soup_plate import SoupPlate

if __name__ == "__main__":

    plate_manager = PlateManager()
    plate_manager.add_plate(SoupPlate(12.5, "Ceramic", "Red", False, True, {"soup", "stew"}, 10, "borsch"))
    plate_manager.add_plate(
        SaladPlate(24, "Faience", "Gray", True, True, "oval", True, {"salad", "vegetables"}))
    plate_manager.add_plate(
        SaladPlate(30, "Porcelain", "Black", False, True, "rectangle", True, {"salad", "vegetables"}))
    plate_manager.add_plate(SoupPlate(40.3, "Ceramic", "Gray", True, True, {"soup", "stew"}, 15, "Mushroom broth"))
    plate_manager.add_plate(PicnicPlate(54, "Faience", "Red", False, False, True, 5, {"sandwich", "fruit", "chips"}))
    plate_manager.add_plate(DessertPlate(60, "Porcelain", "Yellow", True, True, True, 3, {"cake", "ice cream"}))
    plate_manager.add_plate(PicnicPlate(74, "Faience", "Red", False, True, True, 7, {"sandwich", "fruit", "chips"}))
    plate_manager.add_plate(DessertPlate(80, "Porcelain", "Pink", True, True, False, 4, {"cake", "ice cream"}))

    for plate in plate_manager.plate_list:
        print(plate)
    print('\n')
    plate_manager.find_plate_with_diameter_greater_than(30)
    print('\n')
    plate_manager.find_all_clean()
    print('\n')
    plate_manager.plate_enumerate()
    print('\n')
    plate_manager.get_max_food_weight_list()
    print('\n')
    print(plate_manager.plate_zip())

    plate = SoupPlate(12, "Ceramic", "Red", False, True, {"soup", "stew"}, 10, "borsch")

    print(plate.get_attributes_by_type(bool))


    def altitude_condition(some_plate):
        return some_plate.has_food

    result = plate_manager.check_conditions(altitude_condition)
    print(result)

    set_manager = SetManager(plate_manager)

    for food_item in set_manager:
        print(food_item)

    @call_history("file_name")
    def add(a, b):
        return a+b

    add(1,2)
