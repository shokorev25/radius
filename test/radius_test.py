import math
import pytest
from main.radius import calculate_circle_area

def test_calculate_circle_area():
    assert calculate_circle_area(0) == 0
    assert calculate_circle_area(1) == math.pi
    assert calculate_circle_area(2.5) == math.pi * (2.5 ** 2)
    with pytest.raises(ValueError):
        calculate_circle_area(-1)

if __name__ == "__main__":
    pytest.main(["-v"])  
