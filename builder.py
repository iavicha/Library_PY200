from Driver import JsonFileDriver
from Driver import CsvFileDriver


class DriverBuilder:
    def build(self):
        return None


class JsonFileBuilder(DriverBuilder):
    def build(self):
        filename = input('Введите названия файла')
        return JsonFileDriver(filename)


class CsvFileBuilder(DriverBuilder):
    def build(self):
        filename = input('Введите названия файла')
        return CsvFileDriver(filename)


class FabricBuilders:
    @staticmethod
    def fabric_driver():
        driver_name = input('Where you prefer save the file?')

        drivers = {
            'json_file': JsonFileBuilder,
            'csv_file': CsvFileBuilder

        }

        return drivers[driver_name]().build()


if __name__ == '__main__':

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    driver = FabricBuilders.fabric_driver()
    driver.write(l)
