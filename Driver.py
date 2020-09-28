import json
import csv


class MyFilesDriver:
    def read(self):
        pass

    def write(self, data):
        pass


class JsonFileDriver(MyFilesDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> list:
        with open(self.filename, 'r') as json_file:
            return json.load(json_file)

    def write(self, data) -> None:
        with open(self.filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, sort_keys=False, ensure_ascii=False)


class CsvFileDriver(MyFilesDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return csv.reader(csvfile=file)

    def write(self, data) -> None:
        with open(self.filename, 'w') as csv_file:
            csv.writer(csv_file, data)
