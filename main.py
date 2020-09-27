import json


a = dict()


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
        self.books_in_libary = books_in_library if not None else []

    def search(self):
        pass

    def add_book(self):

        author = input('author\n')
        name = input('name\n')
        date = input('date\n')
        cover = input('cover\n')
        about = input('about\n')
        book = Book(author, name, date, cover, about)
        b.append(book)

    def dell_book(self):
        pass

    def get_book(self):
        pass

    def __find_by_author(self, author_to_find: str ):

        author_to_find = author_to_find.title()

        for book in self.books_in_library:
            print(i)
            if atf.title() == i.author.title():
                k = f'Найдены {i.author.title()} книги {i.name.title()}'
                print(k)
                result.append(k)
            else:
                pass



class Console():

    def find_book(self):
        pass



class How_to_start():

    # def __cover__(self):
    #     image = Image.open(self.cover)
    #     image.show()


def set_book():
    pass




def get_books(b):
    for _ in range(len(b)):
        print(_)
        a[b[_].author] = (b[_].name, b[_].date, b[_].cover, b[_].about)
        print([b[_].author])
    make_json(a)


# Не работает метод сортировки по алфавиту


def make_json(a):
    with open('data.json', 'w', encoding='utf-8') as kar:
        json.dump(a, kar, sort_keys=False, ensure_ascii=False)


def load_json():
    with open('data.json', 'r+') as kar:
        a = json.load(kar)
        print(kar)
        # book = Book(author, name, date, cover, about)


def find_book(b):
    result = list()
    wtf = input('Введите параметр для поиска, 1 - автор, 2 - название\n')
    if wtf == '1':
        atf = input('Введите автора\n')

    elif wtf == '2':
        ntf = input('Введите название')
        for i in b:
            if ntf.title() == i.name.title():
                k = f'Найдены книги {i.name.title()} автор {i.author.title()} '
                result.append(k)
            else:
                pass
    if len(result) == 0:
        print('Ничего не найдено')
    print(result)


# set_book()

# for i in range(len(b)):
#     print(b[i].author.title())



# load_json()

if __name__ == '__main__':

    start = input('Введите ещё одну книу 1 - Yes, 2 - NO, 3 - выолнить поиск по книгам\n')
    if start == '1':
        set_book()
        print(b)
    elif start == '2':
        print(b)
        get_books(b)
    elif start == '3':
        get_books(b)
        find_book(b)