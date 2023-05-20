from models.Plate import Plate


class PlateManager:
    __plate_list = list()

    def add_plate(self, plate: Plate):
        self.plate_list.append(plate)

    def find_plate_with_diameter_greater_than(self, value: float):
        print(f'All plates with diameter greater than {value}cm:')
        filtered_plates = [plate for plate in self.plate_list if plate.diameter > value]
        for plate in filtered_plates:
            print(plate)

    def find_all_clean(self):
        print(f'All clean')
        filtered_plates = [plate for plate in self.plate_list if plate.is_clean]
        for plate in filtered_plates:
            print(plate)

    @property
    def plate_list(self):
        return self.__plate_list
