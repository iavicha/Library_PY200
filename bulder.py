from Driver import JsonFileDriver
from Driver import CsvFileDriver


class DriverBuilder(self):
    def build(self):
        return None


class JsonFileBuilder(self):
    pass


class CsvFileBuilder(self):
    pass


class FabricBuilders(self):
    @staticmethod
    def fabric_driver():
        driver_name = input('Where you prefer save the file?')

        driver = {
            'json_file': JsonFileDriver,
            'csv_file': CsvFileDriver

        }


