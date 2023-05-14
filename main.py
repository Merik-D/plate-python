from Plate import Plate

if __name__ == "__main__":

    plates = [Plate(12.3, "ceramic", "red", True, True),
              Plate(),
              Plate.get_instance(),
              Plate.get_instance()]

    for plate in plates:
        print(plate)