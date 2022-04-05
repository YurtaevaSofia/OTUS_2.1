from src.Triangle import Triangle


def test_triangle_exists():
    triangle = Triangle(13, 14, 15)
    assert triangle.a == 13
    assert triangle.b == 14
    assert triangle.c == 15


def test_triangle_not_exists():
    triangle = Triangle(13, 140, 15)
    assert triangle is None


def test_triangle_area_count():
    triangle = Triangle(3, 4, 5)
    assert triangle.area == 6


def test_unexisting_triangle_area_count():
    triangle = Triangle(30, 4, 5)
    assert triangle is None


def test_triangle_perimetr_count():
    triangle = Triangle(6, 4, 5)
    assert triangle.perimetr == 15
