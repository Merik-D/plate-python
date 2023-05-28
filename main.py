from manager.plate_manager import PlateManager
from models.dessert_plate import DessertPlate
from models.picnic_plate import PicnicPlate
from models.salad_plate import SaladPlate
from models.soup_plate import SoupPlate

if __name__ == "__main__":

    plate_manger = PlateManager()
    plate_manger.add_plate(SoupPlate(12, "Ceramic", "Red", False, True, 10, "borsch"))
    plate_manger.add_plate(SaladPlate(24, "Faience", "Gray", True, True, "oval", True))
    plate_manger.add_plate(SaladPlate(30, "Porcelain", "Black", False, True, "rectangle", True))
    plate_manger.add_plate(SoupPlate(40, "Ceramic", "Gray", True, True, 15, "Mushroom broth"))
    plate_manger.add_plate(PicnicPlate(54, "Faience", "Red", False, True, True, 5))
    plate_manger.add_plate(DessertPlate(60, "Porcelain", "Yellow", True, True, True, 3))
    plate_manger.add_plate(PicnicPlate(74, "Faience", "Red", False, True, True, 7))
    plate_manger.add_plate(DessertPlate(80, "Porcelain", "Pink", True, True, False, 4))

    for plate in plate_manger.plate_list:
        print(plate)
    print('\n')
    plate_manger.find_plate_with_diameter_greater_than(30)
    print('\n')
    plate_manger.find_all_clean()
