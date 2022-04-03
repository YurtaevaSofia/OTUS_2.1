from math import pi

from src.Figure import Figure


class Circle(Figure):
    name = "Cirlce"

    def __init__(self, r):
        self.r = r

    @property
    def perimetr(self):
        return 2 * pi * self.r

    @property
    def area(self):
        return pi * self.r * self.r
