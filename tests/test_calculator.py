"""
Test suite for the Calculator class.
"""

import pytest
from src.calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_from_negative(self):
        """Test subtracting positive from negative number."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_from_positive(self):
        """Test subtracting negative from positive number."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero(self):
        """Test subtracting zero from a number."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_from_zero(self):
        """Test subtracting a number from zero."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 5.5
        b = 2.3
        expected = 3.2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero_by_number(self):
        """Test multiplying zero by a number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 1
        expected = 5

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 4.0
        expected = 10.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -10
        b = -2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_by_negative(self):
        """Test dividing positive by negative number."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -2
        expected = -5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_by_positive(self):
        """Test dividing negative by positive number."""
        # Arrange
        calc = Calculator()
        a = -10
        b = 2
        expected = -5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_one(self):
        """Test dividing by one."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 1
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_zero(self):
        """Test dividing by zero raises exception."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 7.5
        b = 2.5
        expected = 3.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_with_remainder(self):
        """Test dividing numbers that result in a decimal."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 3.333333

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected, rel=1e-5)
