from loguru import logger
from SQLbase import SqlBaseClass

logger.add('log.info', format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


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
        # self.books_in_library = if books_in_library is  None else []
        # logger.info({self.books_in_library})
        pass

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
        return book
        # self.books_in_library.append(self.book)

    def edit_book(self):
        pass

    def dell_book(self):
        pass

    def get_book(self):
        pass

    def __find_by_author(self, author_to_find: str):
        # author_to_find = author_to_find.title()
        # for book in self.books_in_library:
        #     print(i)
        #     if atf.title() == i.author.title():
        #         k = f'Найдены {i.author.title()} книги {i.name.title()}'
        #         print(k)
        #         result.append(k)
        #     else:
        pass

    def __find_by_name(self, name_to_find: str):
        # ntf = input('Введите название')
        # for i in b:
        #     if ntf.title() == i.name.title():
        #         k = f'Найдены книги {i.name.title()} автор {i.author.title()} '
        #         result.append(k)
        pass

    def __find_be_year(self, ):
        pass

        def __read(self):
            pass

        def __write(self):
            pass


class Console:
    """
    Данный класс определяет взаимодействие с пользователем через интерфейс коммандной строки
    """

    def start_screen(self):
        info_start_screen = "Что необходимо сделать?\n1 -Работа с базой данных\n\
2 -Работа в режиме библитека-список в оперативной памяти\n3 -Добавть книгу \n\
4 -Работа с файламаи в формате Json\n5 -Работа с файлами в формате CSV\n\
6 -Работа с базой данных\n"
        logger.debug('Запрос у пользователя на выбор данных')
        print(info_start_screen)
        what_to_do_start_screen = input('\n')
        if what_to_do_start_screen == '1':
            logger.debug('Запрос открытия базы')
            Console().screen_sql_first()
        elif what_to_do_start_screen == '2':
            pass
        elif what_to_do_start_screen == '3':
            Console().screen_book()
            logger.debug('Запрос открытия меню книги')
        elif what_to_do_start_screen == '4':
            pass
        elif what_to_do_start_screen == '5':
            pass
        elif what_to_do_start_screen == '6':
            pass
        else:
            exit()

    def screen_book(self):
        info_screen_book = "1 - Добавить книгу\n2 - Удалить книгу\n3 - Найти книгу\n4 - Сохранить книгу в БД\n \
5- Перейти к меню выбора\n"
        print(info_screen_book)
        logger.debug('Вызов экрана работы с книгой')
        what_to_do_screen_book = input('\n')
        if what_to_do_screen_book == '1':
            logger.debug('Запрос добавить книгу')
            Library().add_book()
            Console().screen_book()
        elif what_to_do_screen_book == '2':
            pass
        elif what_to_do_screen_book == '3':
            pass
        elif what_to_do_screen_book == '4':
            pass
        elif what_to_do_screen_book == '5':
            Console().start_screen()
            logger.debug('Вызов главного меню')
            pass

    def screen_json(self):
        info_screen_json = "1 - Создать файл Json\n2 - Открыть файл Json\n"
        print(info_screen_json)
        logger.debug("Вызов экрана работы с Json")
        what_to_do_json = input('\n')
        if what_to_do_json == "1":
            pass
        if what_to_do_json == '2':
            pass
        if what_to_do_json == '3':
            pass

    def screen_csv(self):
        info_screen_csv = "1 - Создать файл csv\n2 - Открыть файл Json\n "
        print(info_screen_csv)
        logger.debug('Вызов экрана работы с CSV')
        what_to_do_csv = input('\n')
        if what_to_do_csv == '1':
            pass
        if what_to_do_csv == '2':
            pass

    def screen_sql_first(self):
        name_of_base = input('Введите имя файла для бд') + '.db'
        Console().screen_sql(name_of_base)

    def screen_sql(self, name_of_base):
        info_screen_sql = '1 - Создать базу данных \n2 - Добавить книгу В БД \n3 - Поиск в базе данных по автору\n\
4 - Открыть в базе данных по имени\n5 - Открыть в базе данных по году\n6 - Закрыть базу данных\n'
        print(info_screen_sql)
        logger.debug('Вызов экрана работы с SQL')
        what_to_do_sql = input('/n')
        if what_to_do_sql == '1':
            SqlBaseClass(name_of_base)
            Console().screen_sql(name_of_base)
        elif what_to_do_sql == '2':
            book = Library().add_book()
            SqlBaseClass(name_of_base, None, book).adder()
            Console().screen_sql(name_of_base)
        elif what_to_do_sql == '3':
            search_author = input('Введите автора\n')
            SqlBaseClass(name_of_base).finder_by_author(search_author)
            Console().screen_sql(name_of_base)
        elif what_to_do_sql == '4':
            search_tittle = input('Введите название\n')
            SqlBaseClass(name_of_base).finder_by_tittle(search_tittle)
            Console().screen_sql(name_of_base)
        elif what_to_do_sql == '5':
            search_year = input('Введите год\n')
            SqlBaseClass().finder_by_tittle(search_year)
            Console().screen_sql(name_of_base)
        elif what_to_do_sql == '6':
            SqlBaseClass(name_of_base).closer()
            Console().start_screen(name_of_base)


if __name__ == '__main__':
    Console().start_screen()
