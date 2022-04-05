from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"

    def __new__(cls, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            obj = object.__new__(cls)
            return obj
        else:
            return None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimetr(self):
        if self.a is not None:
            return self.a + self.b + self.c
        else:
            return 0

    @property
    def area(self):
        if self.a is not None:
            return sqrt(self.perimetr / 2 * (self.perimetr / 2 - self.a) * (self.perimetr / 2 - self.b) * (
                    self.perimetr / 2 - self.c))
        else:
            return 0
