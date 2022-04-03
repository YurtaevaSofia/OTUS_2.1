from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_adding_area_for_two_same_figures():
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(3, 4, 5)
    summ_area = triangle1.add_area(triangle2)
    assert summ_area == 12


def test_adding_area_for_two_different_figures():
    rectangle = Rectangle(3, 4)
    square = Square(6)
    summ_area = rectangle.add_area(square)
    assert summ_area == 48


def test_adding_area_for_two_other_different_figures():
    triangle1 = Triangle(3, 4, 5)
    circle = Circle(6)
    summ_area = triangle1.add_area(circle)
    assert summ_area == 119.09733552923255


def test_adding_area_for_not_existing_triangle():
    triangle1 = Triangle(3, 4, 50)
    circle = Circle(6)
    summ_area = triangle1.add_area(circle)
    assert summ_area == circle.area
