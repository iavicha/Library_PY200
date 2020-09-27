import sqlite3


class DataBase:
    def adder(self):
        pass

    def finder(self):
        pass

    def editor(self):
        pass

    def new_base(self):
        pass

    def choise_base(self):
        pass


class SqlBase(DataBase):

    def choise_base(self):
        base = sqlite3.connect('database.db')
        return base

    def new_base(self):
        c = base.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books 
                     (a_title, an_author, year, about)''')

    def adder(self):
        c.execute("INSERT INTO books VALUES  ('Mark Twen', 'Tom Soyer', 1960, 'about_one bad boy')")


    def finder(self):
        c.execute('select an_author from books where a_title =:title', {'title': 'Mark Twen'})
        return c.fetchone()
        base.close()
