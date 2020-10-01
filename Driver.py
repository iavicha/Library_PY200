import json
import csv
from loguru import logger

logger.add('log_driver.info', compression='zip', format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


class MyFilesDriver:
    def read(self):
        pass

    def write(self, data):
        pass


@logger.catch(level='DEBUG')
class JsonFileDriver(MyFilesDriver):
    def __init__(self, filename: str):
        self.filename = filename + '.json'
        logger.info(f'Присвоено имя файла Json {self.filename}')

    def read(self) -> list:
        with open(self.filename, 'r') as json_file:
            logger.info(f'Чтение файла Json {self.filename}')
            return json.load(json_file)

    def write(self, data) -> None:
        with open(self.filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, sort_keys=False, ensure_ascii=False)
            logger.info(f'Запись файла Json {self.filename}')

@logger.catch(level='DEBUG')
class CsvFileDriver(MyFilesDriver):
    def __init__(self, filename: str):
        self.filename = filename + 'csv'
        logger.info(f'Присвоено имя файла CSV {self.filename}')

    def read(self):
        with open(self.filename, 'r') as file:
            logger.info(f'Чтение файла CSV {self.filename}')
            return csv.reader(csvfile=file)

    def write(self, data) -> None:
        with open(self.filename, 'w') as csv_file:
            book_csv_writer = csv.writer(csv_file, delimiter=' ',
                                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
            book_csv_writer.writerow(data)
            logger.info(f'Запись файла CSV {self.filename}')
