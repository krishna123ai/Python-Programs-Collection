"""Factorial Program in Python.

This module provides a function to calculate the factorial of a non-negative
integer using an iterative approach.
"""


def calculate_factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer n iteratively."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    test_numbers = [0, 1, 5, 7, 10]
    print("--- Factorial Program Demonstration ---")
    for num in test_numbers:
        fact = calculate_factorial(num)
        print(f"Factorial of {num} is: {fact}")


if __name__ == "__main__":
    main()
