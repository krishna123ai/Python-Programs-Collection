"""Fibonacci Sequence Generator in Python.

This module provides a function to generate the first n terms of the
Fibonacci sequence iteratively.
"""


def generate_fibonacci(n: int) -> list[int]:
    """Generate a list containing the first n Fibonacci numbers.

    Terms: 0, 1, 1, 2, 3, 5, 8, ...
    """
    if not isinstance(n, int):
        raise TypeError("Number of terms n must be an integer.")
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")
    if n == 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence


def main():
    test_counts = [0, 1, 2, 7, 10]
    print("--- Fibonacci Sequence Demonstration ---")
    for count in test_counts:
        fib_seq = generate_fibonacci(count)
        print(f"First {count} terms: {fib_seq}")


if __name__ == "__main__":
    main()
