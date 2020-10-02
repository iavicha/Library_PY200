from Driver import JsonFileDriver
from Driver import CsvFileDriver
from loguru import logger
from main import Book

logger.add('log_builder.info', compression='zip', format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


class DriverBuilder:
    def build(self):
        return None


class JsonFileBuilder(DriverBuilder):
    def build(self):
        filename = input('Введите названия файла')
        logger.info('Вызов драйвера Json')
        return JsonFileDriver(filename)


class CsvFileBuilder(DriverBuilder):
    def build(self):
        filename = input('Введите названия файла')
        logger.info('Вызов драйвера CSV')
        return CsvFileDriver(filename)


class FabricBuilders:
    @staticmethod
    def fabric_driver():
        driver_name = input('Where you prefer save the file?\n')

        drivers = {
            'json_file': JsonFileBuilder,
            'csv_file': CsvFileBuilder

        }
        logger.info('Вызов фабрики драйверов')
        return drivers[driver_name]().build()


if __name__ == '__main__':
    book = Book(author='Tolkien',
                name='Hobbit',
                date='1937',
                cover='Null',
                about='about one little man in this big world')

    book1 = Book(author='Tolkien',
                 name='Lord of the rings',
                 date='1937',
                 cover='Null',
                 about='about one little man in this big world')

    books = [book, book]
    books_to_write = {'author':[i.author for i in books], 'name': [i.name for i in books], 'date':
                         [i.date for i in books]}
    print(books_to_write)

    driver = FabricBuilders.fabric_driver()
    l = driver.read()
    print(l)