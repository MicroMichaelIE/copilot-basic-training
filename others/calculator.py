from typing import Union, Optional

class CalculatorError(Exception):
    """Custom exception for calculator operations"""
    pass

class Calculator:
    """A simple calculator class implementing basic arithmetic operations"""
    
    def __init__(self) -> None:
        """Initialize the calculator"""
        self.last_result: Optional[float] = None
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers"""
        try:
            self.last_result = float(a + b)
            return self.last_result
        except TypeError:
            raise CalculatorError("Invalid input types for addition")
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract b from a"""
        try:
            self.last_result = float(a - b)
            return self.last_result
        except TypeError:
            raise CalculatorError("Invalid input types for subtraction")
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers"""
        try:
            self.last_result = float(a * b)
            return self.last_result
        except TypeError:
            raise CalculatorError("Invalid input types for multiplication")
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b"""
        try:
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            self.last_result = float(a / b)
            return self.last_result
        except TypeError:
            raise CalculatorError("Invalid input types for division")
        except ZeroDivisionError as e:
            raise CalculatorError(str(e))
    
    def get_last_result(self) -> Optional[float]:
        """Return the last calculation result"""
        return self.last_result

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))       # 8.0
    print(calc.subtract(10, 4)) # 6.0
    print(calc.multiply(2, 3))  # 6.0
    print(calc.divide(15, 3))   # 5.0


from others.calculator import Calculator, CalculatorError
import pytest

def test_calculator_initialization():
    calc = Calculator()
    assert calc.get_last_result() is None

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0
    assert calc.add(-1, 1) == 0.0
    assert calc.add(1.5, 2.5) == 4.0
    
def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2.0
    assert calc.subtract(1, 1) == 0.0
    assert calc.subtract(2.5, 1.5) == 1.0

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6.0
    assert calc.multiply(-2, 3) == -6.0
    assert calc.multiply(2.5, 2) == 5.0

def test_division():
    calc = Calculator()
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3.0

def test_last_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.get_last_result() == 5.0
    calc.subtract(5, 2)
    assert calc.get_last_result() == 3.0

def test_invalid_input_types():
    calc = Calculator()
    with pytest.raises(CalculatorError):
        calc.add("1", 2)
    with pytest.raises(CalculatorError):
        calc.subtract([], 2)
    with pytest.raises(CalculatorError):
        calc.multiply({}, 2)
    with pytest.raises(CalculatorError):
        calc.divide(1, "2")

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(CalculatorError) as exc_info:
        calc.divide(5, 0)
    assert str(exc_info.value) == "Division by zero is not allowed"