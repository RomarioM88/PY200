class Rectangle:
    def __init__(self, height, width):
        """    Создание и подготовка к работе объекта "Прямоугольник"
               :param height: высота
               :param width: ширина
               Методы: get_perimetr и get_area считают периметр и площадь фигуры
                Пример инициализация экземпляра класса приведен ниже.
               """
        if not isinstance(height, int):
            raise TypeError("Тип должен быть int")
        if not isinstance(width, int):
            raise TypeError("Тип должен быть int")
        self.height = height
        self.width = width

    def get_perimetr(self):
        perimetr = self.height * 2 + self.width * 2
        return perimetr

    def get_area(self):
        area = self.height * self.width
        return area

    def get_info(self):
        p = self.get_perimetr()
        a = self.get_area()
        print('У прямоугольника периметр = %s площадь = %s' % (p, a))


class Circle:
    def __init__(self, radius):
        """    Создание и подготовка к работе объекта "Круг"
               :param radius: радиус круга
               Методы: get_perimetr и get_area считают периметр и площадь фигуры
               Пример инициализация экземпляра класса приведен ниже.
               """
        if not isinstance(radius, int):
            raise TypeError("Тип должен быть int")
        if radius < 0:
            raise ValueError("Радиус должен быть положительный")
        self.radius = radius

    def get_perimetr(self):
        perimetr = round((2 * 3.14 * self.radius), 2)
        return perimetr

    def get_area(self):
        area = round((3.14 * self.radius ** 2), 2)
        return area

    def get_info(self):
        p = self.get_perimetr()
        a = self.get_area()
        print('У круга периметр = %s площадь = %s' % (p, a))


if __name__ == '__main__':
    fig1 = Rectangle(5, 5)
    fig2 = Rectangle(10, 10)
    array = [fig1, fig2]
    for f in array:
        f.get_info()
    fig3 = Circle(5)
    fig4 = Circle(10)
    array2 = [fig3, fig4]
    for f in array2:
        f.get_info()
