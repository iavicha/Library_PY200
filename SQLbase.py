import sqlite3
from loguru import logger


class DataBase():
    def adder(self):
        pass

    def finder(self):
        pass

    def editor(self):
        pass

    def new_base(self):
        pass

    def choice_base(self):
        pass


class SqlBaseClass(DataBase):

    def __init__(self, filename_base: str):
        self.base = sqlite3.connect(filename_base)
        self.c = self.base.cursor()

    def new_base(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS books 
                     (a_title, an_author, year, about)''')
        self.base.commit()

    def adder(self):
        self.c.execute("INSERT INTO books VALUES  ('Mark Twen', 'Tom Sower', 1960, 'about_one bad boy')")
        self.base.commit()

    def finder(self):
        self.c.execute('select an_author from books where a_title =:title', {'title': 'Mark Twen'})
        return self.c.fetchall()

    def closer(self):
        self.base.close()


sql_base = SqlBaseClass('database.db')

# sql_base.new_base()
# sql_base.adder()
# sql_base.closer()


print(sql_base.finder())
