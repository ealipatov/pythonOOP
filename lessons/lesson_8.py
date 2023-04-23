class Point:
    MIN = - 100
    MAX = 100
    DEFAULT_VALUE = 0

    @classmethod    
    def __check_value(cls, value):
        return value if cls.MIN <= value <= cls.MAX else cls.DEFAULT_VALUE

    def __init__(self, x, y):  # Обычный метод
        self.__x = self.__check_value(x)
        self.__y = self.__check_value(y)
        # self.__x = self.__y = 0
        # if self.MIN <= x <= self.MAX:
        #     self.__x = x
        # if self.MIN <= y <= self.MAX:
        #     self.__y = y

    def __str__(self):  # Обычный метод
        return f"x:{self.__x} y:{self.__y}"

    def set_x(self, x):
        self.__x = self.__check_value(x)

    def set_y(self, y):
        self.__y = self.__check_value(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


point1 = Point(10, 50)
point2 = Point(30, 40)
point2.set_x(80)

print(point1.get_x())
print(point2)
