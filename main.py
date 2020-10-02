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


class Console:

    """
    Данный класс определяет взаимодействие с пользователем через интерфейс коммандной строки
    """

    def start_screen(self):
        info_start_screen = "Что необходимо сделать?\n1 -Открыть базу данных\n\
2 -Работа в режиме библитека-список в оперативной памяти\n3 -Добавть книгу \n\
4 -Работа с файламаи в формате Json\n5 -Работа с файлами в формате CSV\n\
6 -Работа с базой данных\n"
        logger.debug('Запрос у пользователя на выбор данных')
        print(info_start_screen)
        what_to_do_start_screen = input('\n')
        if what_to_do_start_screen == '1':
            logger.debug('Запрос открытия базы')
        elif what_to_do_start_screen == '2':
            pass
        elif what_to_do_start_screen == '3':
            pass
        elif what_to_do_start_screen == '4':
            pass
        elif what_to_do_start_screen == '5':
            pass
        elif what_to_do_start_screen == '6':
            pass
        else:
            exit()



    def screen_book(self):
        info_screen_book = "1 - Добавить книгу\n2 - Удалить книгу\n3 - Найти книгу\n4 - Сохранить книгу\n \
4 - Перейти к меню выбора\n"
        print(info_screen_book)
        logger.debug('Вызов экрана работы с книгой')
        pass

    def screen_json(self):
        info_screen_json = "1 - Создать файл Json\n2 - Открыть файл Json\n"
        print(info_screen_json)
        logger.debug("Вызов экрана работы с Json")


    def screen_csv(self):
        info_screen_csv = "1 - Создать файл csv\n2 - Открыть файл Json\n "
        print(info_screen_csv)
        logger.debug('Вызов экрана работы с CSV')

    def screen_sql(self):
        info_screen_sql = '1 - Создать базу данных\n2 - Открыть базу данных\n3 - Поиск в базе данных по автору\n\
4 - Открыть в базе данных по имени\n5 - Открыть в базе данных по году\n6 - Закрыть базу данных\n'
        print(info_screen_sql)
        logger.debug('Вызов экрана работы с SQL')




if __name__ == '__main__':

    Console().start_screen()
    # Console().screen_book()
    # Console().screen_json()
    # Console().screen_csv()
    # Console().screen_sql()

    # start = input('Введите ещё одну книу 1 - Yes, 2 - NO, 3 - выолнить поиск по книгам\n')
    # if start == '1':
    #     Library().add_book()
    #
    # elif start == '2':
    #     get_books(b)
    # elif start == '3':
    #     find_book(b)
