class IntegerCoordinate:
    MIN_VALUE = 0
    MAX_VALUE = 100

    @classmethod
    def validate_coordinate(cls, coordinate):
        if type(coordinate) == int and cls.MIN_VALUE <= coordinate <= cls.MAX_VALUE:
            return coordinate
        else:
            return 0

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        return setattr(instance, self.name, self.validate_coordinate(value))


class Point:
    x = IntegerCoordinate()
    y = IntegerCoordinate()
    z = IntegerCoordinate()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point = Point(1, 2, "asd")
print(point.x, point.y, point.z)
