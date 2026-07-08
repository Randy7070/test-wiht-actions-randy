# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 3 #lo rompi al proposito


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 999 #lo rompi al proposito 
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
