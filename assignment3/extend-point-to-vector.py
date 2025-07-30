import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_equal_to(self, other):
        return self.x == other.x and self.y == other.y

    def describe(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vector(Point):
    def describe(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

