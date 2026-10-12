class Vector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f'Vector x={self.x}, y={self.y}, z={self.z}'

v1= Vector(1, 2, 3)
v2= Vector(4, 5, 6)
v3= v1 + v2
print(v3)
print(v1 - v2)
