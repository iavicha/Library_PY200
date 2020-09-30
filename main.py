from loguru import logger
logger.add('log.info', compression='zip', format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


class Book:

    def __init__(self, author, name, date, cover, about):
        self.author = author
        self.name = name
        self.date = date
        self.cover = cover
        self.about = about
        logger.debug('Создана книга')


class Library:

    def __init__(self, books_in_library: list = None):
        # self.where_to_write = where_to_write
        self.books_in_library = books_in_library if not None else []

    def search(self):
        pass

    @logger.catch(level='DEBUG')
    def add_book(self):
        author = input('author\n')
        name = input('name\n')
        date = input('date\n')
        cover = input('cover\n')
        about = input('about\n')
        book = Book(author, name, date, cover, about)
        logger.debug('Добавлена книга')
        self.books_in_library.append(self.book)

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

    def hello(self):
        print("Что необходимо сделать?\n")
        print()

    def find_book(self):
        pass

    #
    # def set_book():
    #     pass

    def get_books(b):
        for _ in range(len(b)):
            print(_)
            a[b[_].author] = (b[_].name, b[_].date, b[_].cover, b[_].about)
            print([b[_].author])
        make_json(a)


if __name__ == '__main__':

    start = input('Введите ещё одну книу 1 - Yes, 2 - NO, 3 - выолнить поиск по книгам\n')
    if start == '1':
        Library().add_book()
    #
    # elif start == '2':
    #     get_books(b)
    # elif start == '3':
    #     find_book(b)
