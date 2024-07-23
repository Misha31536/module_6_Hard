class Figure:

    sides_count = 0

    def __init__(self,__sides, __color, filled):
        self.__sides = int(__sides)
        self.__color = list(__color)
        self.filled = bool(filled)


    def get_color(self, color):
        if self.__is_valid_color(color): # если метод проверки цвета True
            c self.__color
            return color

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
                return
            else:
                print("Цвет должен быть написано цифрами и в диапазоне от 0 до 255")





class Circle():
    pass

class Triangle():
    pass

class Cube():
    pass

circle1 = Figure(200, [], 100)
print(circle1.get_color([200,200,200]))

