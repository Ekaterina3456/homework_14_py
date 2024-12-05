# Напишите класс Rectangle, который управляет прямоугольником. Класс должен
# поддерживать следующие методы:
# ● set_dimensions(width, height): устанавливает ширину и высоту
# прямоугольника.
# ● get_area(): возвращает площадь прямоугольника.
# ● get_perimeter(): возвращает периметр прямоугольника.
# Напишите 3 теста с помощью doctest.


class LengthOfSidesError(Exception):
    def __str__(self):
        return 'стороны должны быть больше нуля'


class Rectangle:
    def __init__(self, width, height):
        """
        >>> r = Rectangle(5, 4)
        >>> r.get_area()
        20
        >>> r.get_perimeter()
        18
        >>> r1 = Rectangle(-3, 4)
        Traceback (most recent call last):
        Task_3.LengthOfSidesError: стороны должны быть больше нуля
        """
        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise LengthOfSidesError

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == '__main__':
    rec = Rectangle(10, 4)
    print(rec.get_area())
    print(rec.get_perimeter())