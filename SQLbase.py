import sqlite3
from loguru import logger
from main import Book

logger.add('log_sql.info', compression='zip', format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


class DataBase:
    def connect(self):
        pass

    def adder(self):
        pass

    def finder(self):
        pass

    def editor(self):
        pass

    def new_base(self):
        pass


@logger.catch(level="DEBUG")
class SqlBaseClass(DataBase):

    def __init__(self, filename_base: str, books: list = None, book=None):
        self.base = sqlite3.connect(filename_base)
        self.filename_base = filename_base
        self.c = self.base.cursor()
        self.books = books
        self.book = book
        logger.info('Выполнено подключение к базе данных')

    def connect(self, filename: str = None):
        self.base = sqlite3.connect(filename)
        logger.info('Выполнено подключение к базе данных')

    def new_base(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS books 
                     (a_title, an_author, year, about)''')
        self.base.commit()
        logger.info('Создана таблица базы данных')

    @logger.catch(level='DEBUG')
    def adder(self):
        if self.books is None:
            what_to_add = (self.book.name, self.book.author, self.book.date, self.book.about)
            self.c.execute("INSERT INTO books VALUES  (?, ?, ?, ?)", what_to_add)
        else:
            for i in self.books:
                what_to_add = (i.name, i.author, i.date, i.about)
                self.c.execute("INSERT INTO books VALUES  (?, ?, ?, ?)", what_to_add)
                logger.info('Добавили книгу из списка')
        self.base.commit()
        logger.info('Добавлена книга в базу данных')

    def finder_by_author(self, search_elem=None):
        self.c.execute('select an_author, a_title from books where an_author=:author', {'author': search_elem})
        logger.info(f'Выведен результат поиска {search_elem}')
        return self.c.fetchone()

    def finder_by_tittle(self, search_elem=None):
        self.c.execute('select an_author, a_title from books where a_title=:title', {'title': search_elem})
        logger.info(f'Выведен результат поиска {search_elem}')
        return self.c.fetchone()

    def finder_by_year(self, search_elem=None):
        self.c.execute('select an_author from books where year=:year', {'year': search_elem})
        logger.info(f'Выведен результат поиска {search_elem}')
        return self.c.fetchone()

    def closer(self):
        self.base.close()
        logger.info('Закрыто подключение к базе данных')


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
    logger.info(book1)

    books = [book, book1]
    sql_base = SqlBaseClass('database.db',None , book)

    # sql_base.connect('database.db')
    sql_base.new_base()
    sql_base.adder()
    print(sql_base.finder_by_year('1937'), sql_base.finder_by_author('Tolkien'), sql_base.finder_by_tittle('Hobbit'),
          sql_base.finder_by_tittle('Lord of the rings'))
    sql_base.closer()
