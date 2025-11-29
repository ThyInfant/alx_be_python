# simple_calculator.py
class SimpleCalculator:
  """A simple calculator class that supports basic arithmetic operations."""
  
  def add(self, a, b):
    """Return the addition of a and b."""
    return a + b
  
  def substract(self, a, b):
    """Return the substraction of a and b."""
    return a - b

  def multiply(self, a, b):
    """Return the multiply of a and b."""
    return a * b
  
  def divide(self, a, b):
    """Return the divide of a and b."""
    if b == 0:
      return None
    return a / b