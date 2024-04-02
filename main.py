class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


class Figure(Rectangle, Circle, RightTriangle, Trapezoid):
    def __init__(self, name, shape_type, *args, **kwargs):
        self.name = name
        self.shape_type = shape_type

        if shape_type == "Rectangle":
            Rectangle.__init__(self, *args, **kwargs)
        elif shape_type == "Circle":
            Circle.__init__(self, *args, **kwargs)
        elif shape_type == "RightTriangle":
            RightTriangle.__init__(self, *args, **kwargs)
        elif shape_type == "Trapezoid":
            Trapezoid.__init__(self, *args, **kwargs)

    def area(self):
        if self.shape_type == "Rectangle":
            return Rectangle.area(self)
        elif self.shape_type == "Circle":
            return Circle.area(self)
        elif self.shape_type == "RightTriangle":
            return RightTriangle.area(self)
        elif self.shape_type == "Trapezoid":
            return Trapezoid.area(self)

    def __str__(self):
        return f"{self.name}: {self.shape_type}"


rectangle = Figure("Прямокутник", "Rectangle", 3, 4)
print(f"{rectangle}: {rectangle.area()}")

circle = Figure("Коло", "Circle", 5)
print(f"{circle}: {circle.area()}")

triangle = Figure("Прямокутний трикутник", "RightTriangle", 6, 8)
print(f"{triangle}: {triangle.area()}")

trapezoid = Figure("Трапеція", "Trapezoid", 2, 4, 5)
print(f"{trapezoid}: {trapezoid.area()}")


# Завдання 2
class Figure(Rectangle, Circle, RightTriangle, Trapezoid):
    def __init__(self, name, shape_type, *args, **kwargs):
        self.name = name
        self.shape_type = shape_type

        if shape_type == "Rectangle":
            Rectangle.__init__(self, *args, **kwargs)
        elif shape_type == "Circle":
            Circle.__init__(self, *args, **kwargs)
        elif shape_type == "RightTriangle":
            RightTriangle.__init__(self, *args, **kwargs)
        elif shape_type == "Trapezoid":
            Trapezoid.__init__(self, *args, **kwargs)

    def area(self):
        if self.shape_type == "Rectangle":
            return Rectangle.area(self)
        elif self.shape_type == "Circle":
            return Circle.area(self)
        elif self.shape_type == "RightTriangle":
            return RightTriangle.area(self)
        elif self.shape_type == "Trapezoid":
            return Trapezoid.area(self)

    def __int__(self):
        return int(self.area())

    def __str__(self):
        if self.shape_type == "Rectangle":
            return f"{self.name}: Rectangle\nLength: {self.length}, Width: {self.width}\nArea: {self.area()}"
        elif self.shape_type == "Circle":
            return f"{self.name}: Circle\nRadius: {self.radius}\nArea: {self.area()}"
        elif self.shape_type == "RightTriangle":
            return f"{self.name}: Right Triangle\nBase: {self.base}, Height: {self.height}\nArea: {self.area()}"
        elif self.shape_type == "Trapezoid":
            return f"{self.name}: Trapezoid\nBase1: {self.base1}, Base2: {self.base2}, Height: {self.height}\nArea: {self.area()}"


rectangle = Figure("Прямокутник", "Rectangle", 3, 4)
print(int(rectangle))
print(str(rectangle))

circle = Figure("Коло", "Circle", 5)
print(int(circle))
print(str(circle))

triangle = Figure("Прямокутний трикутник", "RightTriangle", 6, 8)
print(int(triangle))
print(str(triangle))

trapezoid = Figure("Трапеція", "Trapezoid", 2, 4, 5)
print(int(trapezoid))
print(str(trapezoid))
# Завдання 3
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self, filename):
        with open(filename, "w") as f:
            f.write(f"{self.__class__.__name__}|{self.name}\n")

    @abstractmethod
    def load(self, filename):
        pass


class Square(Shape):
    def __init__(self, name, x, y, side_length):
        super().__init__(name)
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Квадрат: {self.name}, ({self.x}, {self.y}), сторона: {self.side_length}")

    def save(self, f):
        f.write(f"Square|{self.name}|{self.x}|{self.y}|{self.side_length}\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.readline().split("|")
            if data[0] == "Square":
                self.name = data[1]
                self.x = int(data[2])
                self.y = int(data[3])
                self.side_length = int(data[4])


class Rectangle(Shape):
    def __init__(self, name, x, y, width, height):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Прямокутник: {self.name}, ({self.x}, {self.y}), ширина: {self.width}, висота: {self.height}")

    def save(self, f):
        f.write(f"Rectangle|{self.name}|{self.x}|{self.y}|{self.width}|{self.height}\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.readline().split("|")
            if data[0] == "Rectangle":
                self.name = data[1]
                self.x = int(data[2])
                self.y = int(data[3])
                self.width = int(data[4])
                self.height = int(data[5])


class Circle(Shape):
    def __init__(self, name, x, y, radius):
        super().__init__(name)
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Коло: {self.name}, ({self.x}, {self.y}), радіус: {self.radius}")

    def save(self, f):
        f.write(f"Circle|{self.name}|{self.x}|{self.y}|{self.radius}\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.readline().split("|")
            if data[0] == "Circle":
                self.name = data[1]
                self.x = int(data[2])
                self.y = int(data[3])
                self.radius = int(data[4])


class Ellipse(Shape):
    def __init__(self, name, x, y, rx, ry):
        super().__init__(name)
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry

    def show(self):
        print(f"Еліпс: {self.name}, ({self.x}, {self.y}), rx: {self.rx}, ry: {self.ry}")

    def save(self, f):
        f.write(f"Ellipse|{self.name}|{self.x}|{self.y}|{self.rx}|{self.ry}\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.readline().split("|")
            if data[0] == "Ellipse":
                self.name = data[1]
                self.x = int(data[2])
                self.y = int(data[3])
                self.rx = int(data[4])
                self.ry = int(data[5])


def add_shape(shapes, shape):
    shapes.append(shape)


def show_all_shapes(shapes):
    for shape in shapes:
        shape.show()


def save_all_shapes(shapes, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for shape in shapes:
            shape.save(f)


def load_all_shapes(shapes, filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data = line.split("|")
            shape_type = data[0]
            if shape_type == "Square":
                shape = Square(data[1], int(data[2]), int(data[3]), int(data[4]))
            elif shape_type == "Rectangle":
                shape = Rectangle(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]))
            elif shape_type == "Circle":
                shape = Circle(data[1], int(data[2]), int(data[3]), int(data[4]))
            elif shape_type == "Ellipse":
                shape = Ellipse(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]))
            else:
                continue
            add_shape(shapes, shape)


shapes = []

square = Square("Квадрат 1", 10, 10, 50)
add_shape(shapes, square)

rectangle = Rectangle("Прямокутник 1", 20, 20, 100, 50)
add_shape(shapes, rectangle)

circle = Circle("Коло 1", 50, 50, 25)
add_shape(shapes, circle)

ellipse = Ellipse("Еліпс 1", 80, 80, 30, 20)
add_shape(shapes, ellipse)

show_all_shapes(shapes)

save_all_shapes(shapes, "shapes.txt")

shapes = []
load_all_shapes(shapes, "shapes.txt")

show_all_shapes(shapes)
