from Driver import JsoneFileDriver
from Driver import CsvFileDriver



class DriverBuilder(self):
    def build(self):
        return None


class JsonFileBulder(self):
    pass


class CsvFileBulder(self):
    pass


class FabricBulders(self):
    @staticmethod
    def fabric_driver():
        driver_name = input('Where you prefer save the file?')

        driver = {
            'json_file': JsoneFileBulder,
            'csv_file': CsvFileBulder

        }
