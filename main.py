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
        # self.books_in_library = if books_in_library is not None else []
        # logger.info({self.books_in_library})

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

    def start_screen(self):
        print("Что необходимо сделать?\n")
        print('1 -Открыть базу данных\n')
        print('2 -Работа в режиме библитека-список в оперативной памяти\n')
        print('3 -Добавть книгу \n')
        print('4 -Работа с файламаи в формате Json')
        print("5 -Работа с файлами в формате CSV")
        print("6 -Работа с базой данных")

        logger.debug('Запрос у пользователя на выбор данных')

    def screen_book(self):
        print('1 - добавить книгу')
        print('2 - Удалить книгу')
        print('3 - Найти книгу')
        print("4 - Перейти к меню выбора ")
        pass

    def screen_json(self):
        pass

    def screnn_CSV(self):
        pass


if __name__ == '__main__':

    Console().start_screen()

    start = input('Введите ещё одну книу 1 - Yes, 2 - NO, 3 - выолнить поиск по книгам\n')
    if start == '1':
        Library().add_book()
    #
    # elif start == '2':
    #     get_books(b)
    # elif start == '3':
    #     find_book(b)
