from src.Square import Square


def test_square_exists():
    square = Square(7)
    assert square.a == 7


def test_square_area_count():
    square = Square(5)
    assert square.area == 25


def test_square_perimetr_count():
    square = Square(9)
    assert square.perimetr == 36
