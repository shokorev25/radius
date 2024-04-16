import math
import pytest
from main.radius import calculate_circle_area

def test_calculate_circle_area_with_zero_radius():
    assert calculate_circle_area(0) == 0

def test_calculate_circle_area_with_radius_one():
    assert calculate_circle_area(1) == math.pi

def test_calculate_circle_area_with_radius_two_point_five():
    assert calculate_circle_area(2.5) == math.pi * (2.5 ** 2)

def test_calculate_circle_area_with_negative_radius():
    with pytest.raises(ValueError):
        calculate_circle_area(-1)
