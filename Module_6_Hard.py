from math import pi
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
        if len(sides) == self.sides_count:
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
                print(self.__sides)

    sides = property(get_sides, set_sides)


    def __len__(self):
        if isinstance(self.__sides, int):
            return self.__sides
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



class Triangle():
    pass

class Cube():
    pass

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
circle1.color = 55, 66, 77 # Изменится
print(circle1.color)
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(circle1.sides)
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())







