from math import pi
class Figure:

    sides_count = 0

    def __init__(self,__sides, __color, filled):
        self.__sides = int(sides)
        self.__color = list(color)
        self.filled = bool(filled)


    def get_color(self):
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

    def set_color(self, color):
        if self.__is_valid_color(color): # если метод проверки цвета True
            self.__color = color
            return self.__color

    def __is_valid_sides(self, *sides):
        if len(sides) == 1:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(sides[0])
                print(self.__sides)
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
            print(self.__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, __sides, __color, filled):
        super().__init__(__sides, __color, filled)

    def __radius(self):
        print(self._Figure__sides)
        r = self._Figure__sides / (2 * pi)
        return r


class Triangle():
    pass

class Cube():
    pass

circle1 = Circle(200, [200,200,200], 100)
a = circle1._Circle__radius()
print(a)
# print(circle1.get_color([200,200,200]))
# print(circle1._Figure__is_valid_sides(1, 2, 4))

