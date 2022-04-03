from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def perimetr(self):
        return (self.a + self.b) * 2

    @property
    def area(self):
        return self.a * self.b
