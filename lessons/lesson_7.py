class Point:
    MIN = - 100
    MAX = 100

    def __init__(self, x, y):  # Обычный метод
        self.x = self.y = 0
        if self.MIN <= x <= self.MAX:
            self.x = x
        if self.MIN <= y <= self.MAX:
            self.y = y

    def __str__(self):  # Обычный метод
        return f"x:{self.x} y:{self.y}"

    @staticmethod
    def sum_point(p1, p2):
        return Point(p1.x + p2.x, p1.y + p2.y)

    @classmethod
    def sum_point_with_check(cls, p1, p2):
        sum_x = p1.x + p2.x
        sum_y = p1.y + p2.y

        return Point(
            sum_x if cls.MIN <= sum_x <= cls.MAX else cls.MAX,
            sum_y if cls.MIN <= sum_y <= cls.MAX else cls.MAX
        )


point1 = Point(10, 50)
point2 = Point(30, 40)
point3 = Point.sum_point(point1, point2)
point4 = Point.sum_point_with_check(point3, point2)
print(point1)
print(point2)
print(point3)
print(point4)