from src.Rectangle import Rectangle


def test_rectangle_exists():
    rectangle = Rectangle(4, 8)
    assert rectangle.a == 4
    assert rectangle.b == 8


def test_rectangle_area_count():
    rectangle = Rectangle(3, 4)
    assert rectangle.area == 12


def test_rectangle_perimetr_count():
    rectangle = Rectangle(6, 4)
    assert rectangle.perimetr == 20
