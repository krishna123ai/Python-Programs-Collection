# Factorial Calculator (Python Basics)

A clean, beginner-friendly Python script to calculate the factorial of a non-negative integer using an iterative approach.

## What the Program Does
- Implements `calculate_factorial(n)` which iteratively multiplies integers from `1` up to `n`.
- Handles edge cases:
  - Factorial of `0` returns `1`.
  - Negative integers raise a `ValueError`.
  - Non-integer types raise a `TypeError`.
- Demonstrates sample executions for `0`, `1`, `5`, `7`, and `10` via a `main()` function.

## How to Run It
Run the script using any Python 3 environment:
```bash
python factorial.py
```

### Sample Output
```
--- Factorial Program Demonstration ---
Factorial of 0 is: 1
Factorial of 1 is: 1
Factorial of 5 is: 120
Factorial of 7 is: 5040
Factorial of 10 is: 3628800
```

## Learning Objectives
- Master iterative loop constructs in Python (`for ... in range(...)`).
- Implement defensive programming and parameter validation (`TypeError`, `ValueError`).
- Organize Python code into reusable functions and entry point guards (`if __name__ == "__main__":`).
