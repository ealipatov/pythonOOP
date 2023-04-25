class Point:
    MIN_VALUE = 0
    MAX_VALUE = 100

    def __init__(self, x, y, z):
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)

    def set_x(self, x):
        self._x = self.validate_coordinate(x)

    def set_y(self, y):
        self._y = self.validate_coordinate(y)

    def set_z(self, z):
        self._z = self.validate_coordinate(z)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    @classmethod
    def validate_coordinate(cls, coordinate):
        if type(coordinate) == int and cls.MIN_VALUE <= coordinate <= cls.MAX_VALUE:
            return coordinate
        else:
            return 0


point = Point(1, 2, "3")
print(point.get_x(), point.get_y(), point.get_z())