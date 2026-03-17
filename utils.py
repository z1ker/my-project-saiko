def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Only integers allowed")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Division by zero")
    return a / b