from loguru import logger
from SQLbase import SqlBaseClass


class Book:

    def __init__(self, author, name, date, cover, about):
        self.author = author
        self.name = name
        self.date = date
        self.cover = cover
        self.about = about


class Library:

    def __init__(self, books_in_library: list = None):
        # self.where_to_write = where_to_write
        self.books_in_library = books_in_library if not None else []

    def search(self):
        pass

    def add_book(self):
        author = input('author\n')
        name = input('name\n')
        date = input('date\n')
        cover = input('cover\n')
        about = input('about\n')
        book = Book(author, name, date, cover, about)
        print(book.author, book.name)
        # self.books_in_libary.append(book)
        # print(self.books_in_libary[0].author)
        return book

    def edit_book(self):
        pass

    def dell_book(self):
        pass

    def get_book(self):
        pass

    def __find_by_author(self, author_to_find: str):

        author_to_find = author_to_find.title()

        for book in self.books_in_library:
            print(i)
            if atf.title() == i.author.title():
                k = f'Найдены {i.author.title()} книги {i.name.title()}'
                print(k)
                result.append(k)
            else:
                pass

    def __find_by_name(self, name_to_find: str):
        ntf = input('Введите название')
        for i in b:
            if ntf.title() == i.name.title():
                k = f'Найдены книги {i.name.title()} автор {i.author.title()} '
                result.append(k)

    def __find_be_year(self, ):

        def __read(self):
            pass

        def __write(self):
            pass


class Console():
    """
    Данный класс определяет взаимодействие с пользователем через интерфейс коммандной строки
    """

    def __repr__(self):
        print("Что необходимо сделать?")

    def find_book(self):
        pass


if __name__ == '__main__':
    library = Library()

    start = input('Введите ещё одну книу 1 - Yes, 2 - NO, 3 - выолнить поиск по книгам\n')
    if start == '1':
        library.add_book()
    #
    # elif start == '2':
    #     get_books(b)
    # elif start == '3':
    #     find_book(b)
