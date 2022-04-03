from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, a):
        self.a = a

    @property
    def perimetr(self):
        return self.a * 4

    @property
    def area(self):
        return self.a * self.a
