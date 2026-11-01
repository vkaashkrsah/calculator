
import pytest

from calculate import calculate


def test_addition():
    expression, result = calculate(20, 10, "add")
    assert result == 30
    assert expression == "20 + 10"


def test_subtraction():
    expression, result = calculate(20, 10, "subtract")
    assert result == 10


def test_multiplication():
    expression, result = calculate(5, 4, "multiply")
    assert result == 20


def test_division():
    expression, result = calculate(20, 5, "divide")
    assert result == 4


def test_modulus():
    expression, result = calculate(20, 3, "mod")
    assert result == 2


def test_percentage():
    expression, result = calculate(20, 200, "percentage")
    assert result == 40


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate(20, 0, "divide")


def test_modulus_by_zero():
    with pytest.raises(ValueError):
        calculate(20, 0, "mod")


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculate(20, 10, "invalid")
