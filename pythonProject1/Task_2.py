# Напишите класс Library, который управляет книгами. Класс должен поддерживать
# следующие методы:
# ● add_book(title): добавляет книгу в библиотеку.
# ● remove_book(title): удаляет книгу из библиотеки.
# ● list_books(): возвращает список всех книг в библиотеке.
# При попытке удалить книгу, которая не существует, должно выбрасываться исключение
# BookNotFoundError. Для тестирования используйте unitest.
import unittest


class TestCheckStr(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add(self):
        self.library.add_book('1984')
        self.assertEquals(self.library.list_books(), '1984')

    def test_remove_success(self):
        self.library.remove_book('1984')
        self.assertEquals(self.library.list_books(), None)

    def test_remove_not_success(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")


class BookNotFoundError(Exception):
    def __str__(self):
        return 'данная книга не найдена в библиотеке'


class Library:

    books = list()

    def __init__(self, ):
        pass

    def add_book(self, title):
        self.books.append(title)

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
        else:
            raise BookNotFoundError

    def list_books(self):
        for book in self.books:
            return book


if __name__ == '__main__':
    unittest.main()
        


