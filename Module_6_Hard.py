from math import pi, sqrt
class Figure:

    sides_count = 0

    def __init__(self, color, sides, filled = False):
        self.__sides = int(sides)
        self.__color = list(color)
        self.filled = bool(filled)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if self.__is_valid_color(color):  # если метод проверки цвета True
            self.__color = color
            return self.__color

    def __is_valid_color(self, color):
        flag = []
        if len(color) == 3:
            for i in range(3):
                if isinstance(color[i], int):
                    if color[i] >= 0 and color[i] <= 255:
                        flag.append(True)
                    else:
                        flag.append(False)
            if all(flag):
                return True
            else:
                print("Цвет должен быть написано цифрами и в диапазоне от 0 до 255")
        else:
            print("Цвет должен быть задан в формате RGB")

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count or len(sides) == 1 :
            flag = []
            for i in range(len(sides)):
                if isinstance(sides[i], int):
                    if sides[i] > 0:
                        flag.append(True)
                    else:
                        flag.append(False)
            if all(flag):
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            if len(new_sides) == 1:
                self.__sides = []
                for i in range(self.sides_count):
                    self.__sides.append(new_sides[0])
                    return self.__sides
            if len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)

    sides = property(get_sides, set_sides)


    def __len__(self):
        if isinstance(self.__sides, int) and self.sides_count == 1:
            return self.__sides
        elif isinstance(self.__sides, int):
            return self.__sides * self.sides_count
        else:
            return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self,  color, sides, filled = False, radius = None):
        super().__init__(color, sides, filled)
        self.__radius = radius

    def __set_radius(self):
        self.__radius = self.sides / (2 * pi)
        print(self.__radius)
        return self.__radius

    def get_square(self):
        self.__set_radius()
        square = pi * self.__radius**2
        return square



class Triangle(Figure):

    sides_count = 3

    def __init__(self,  color, sides, filled = False, height = None):
        super().__init__(color, sides, filled)
        self.__height = height
        self.__set_height()
    #     self.existence()
    #
    # def existence(self):
    #     if isinstance(self.sides, list) and len(self.sides) == 3:
    #         if (self.sides[0] + self.sides[1] > self.sides[2]
    #         and self.sides[0] + self.sides[2] > self.sides[1]
    #             and self.sides[1] + self.sides[2] > self.sides[0]):
    #             print('Треугольник существует')
    #         else:
    #             print("Невозможно построить такой треугольник")
    #             self.__del__()



    def __set_height(self):
        if isinstance(self.sides, int):
            s = self.get_square()
            self.__height = 2 * s / self.sides
            #print(self.__height)
            return self.__height
        else:
            s = self.get_square()
            a = 2 * s /(self.sides[0])
            b = 2 * s / (self.sides[1])
            c = 2 * s / (self.sides[2])
            self.__height = max(a, b, c)
            #print(self.__height)
            return self.__height

    def get_square(self):
        if isinstance(self.sides, int):
            s = self.sides * 3 / 2
            square = sqrt(s * ((s - self.sides) ** 3))
            self.__height = 2 * square / self.sides # высота треугольника
            return square
        else:
            if len(self.sides) > 1:
                s = sum(self.sides) / 2
                heron = 0
                for i in range(len(self.sides)):
                    heron *= (s - self.sides[i])
                square = sqrt(s * heron)
                # высота треугольника
                a = 2 * square / (self.sides[0])
                b = 2 * square / (self.sides[1])
                c = 2 * square / (self.sides[2])
                self.__height = max(a, b, c)
                # # #
                return square
            else:
                s = self.sides[0]*3 / 2
                square = sqrt(s * ((s - self.sides[0]) ** 3))
                self.__height = 2 * square / self.sides[0] # высота треугольника
                return square


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides, filled = False):
        super().__init__(color, sides, filled)
        self.re_sides()

    def re_sides(self):
        n = self.sides
        List_ = [n for i in range(self.sides_count)]
        self.sides = List_


    def get_volume(self):
        V = self.sides[0][0]**3
        return V

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
triangle1 = Triangle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# Проверка на изменение цветов:
# # Реализовано с помощью Декораторов @property

# # # Круг

circle1.color = 55, 66, 77 # Изменится
print(circle1.color)

# # # Треугольник

print(triangle1.color)
triangle1.color = 30, 30 ,30 # Изменится
print(triangle1.color)
triangle1.color = 30, 30 ,-30 # Не Изменится
print(len(triangle1))
triangle1.set_sides(20)
print(triangle1.get_sides())
print(triangle1.get_square())


# # # Куб

cube1.color = 300, 70, 15 # Не изменится
print(cube1.color)
cube1.color = 200, 70, 15 # Не изменится
print(cube1.color)
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

# Реализовано с помощью PROPERTY()

circle1.set_sides(12) # Изменится
print(circle1.get_sides())
print(circle1.sides)

# # Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())






