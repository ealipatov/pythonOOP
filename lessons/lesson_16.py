class Point:
    def __init__(self, x, y, z):
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z
