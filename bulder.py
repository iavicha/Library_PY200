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
        filename = 'csv.csv'
        return CsvFileDriver(filename)


class FabricBuilders:
    @staticmethod
    def fabric_driver():
        driver_name = input('Where you prefer save the file?')

        drivers = {
            'json_file': JsonFileDriver,
            'csv_file': CsvFileDriver

        }

        return drivers[driver_name]().build()


if __name__ == '__main__':

    # driver = FabricBuilders.fabric_driver()
    CsvFileDriver().build()
