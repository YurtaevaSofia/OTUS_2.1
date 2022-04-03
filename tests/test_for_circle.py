from src.Circle import Circle


def test_circle_exists():
    circle = Circle(7)
    assert circle.r == 7


def test_square_area_count():
    circle = Circle(5)
    assert circle.area == 78.53981633974483


def test_circle_length_count():
    circle = Circle(9)
    assert circle.perimetr == 56.548667764616276
