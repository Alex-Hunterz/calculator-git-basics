"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, modulo

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestModulo:
    """Test the modulo operation."""
    
    def test_modulo_positive_integers(self):
        """Test modulo with positive integers."""
        assert modulo(10, 3) == 1
        assert modulo(7, 2) == 1
        assert modulo(20, 5) == 0

    def test_modulo_with_floats(self):
        """Test modulo with floating-point numbers."""
        assert modulo(10.5, 3) == 1.5
        # Use pytest.approx for reliable float comparisons
        assert pytest.approx(modulo(5.5, 2.5)) == 0.5

    def test_modulo_negative_integers(self):
        """Test modulo with negative integers (follows Python's % behavior)."""
        assert modulo(-10, 3) == 2
        assert modulo(10, -3) == -2
        assert modulo(-10, -3) == -1

    def test_modulo_dividend_zero(self):
        """Test modulo where the dividend (a) is zero."""
        assert modulo(0, 5) == 0

    def test_modulo_by_zero_error(self):
        """Test that modulo by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot do 10 modulo by zero - division by zero is undefined"):
            modulo(10, 0)
        
        with pytest.raises(ValueError, match="Cannot do -5 modulo by zero - division by zero is undefined"):
            modulo(-5, 0)

    def test_modulo_non_numeric_inputs(self):
        """
        Test that modulo with non-numeric inputs raises a TypeError.
        Note: Your current modulo function doesn't check for types,
        so this tests the default Python % operator behavior.
        """
        with pytest.raises(TypeError):
            modulo("10", 2)
        
        with pytest.raises(TypeError):
            modulo(10, "2")

