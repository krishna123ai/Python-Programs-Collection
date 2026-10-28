# Fibonacci Generator (Python Basics)

A beginner-friendly Python script to generate the first `n` terms of the Fibonacci sequence iteratively.

## What the Program Does
- Implements `generate_fibonacci(n)` which builds a list containing the first `n` Fibonacci numbers.
- Handles base cases cleanly:
  - `n = 0` produces `[]`
  - `n = 1` produces `[0]`
  - `n >= 2` computes subsequent terms by summing the two preceding elements (`sequence[-1] + sequence[-2]`).
- Performs strict input validation:
  - Raises `TypeError` if `n` is not an integer.
  - Raises `ValueError` if `n` is negative.
- Contains a `main()` function demonstrating outputs for sample terms (`0`, `1`, `2`, `7`, `10`).

## How to Run It
Execute the script using Python:
```bash
python fibonacci.py
```

### Sample Output
```
--- Fibonacci Sequence Demonstration ---
First 0 terms: []
First 1 terms: [0]
First 2 terms: [0, 1]
First 7 terms: [0, 1, 1, 2, 3, 5, 8]
First 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Learning Objectives
- Learn list manipulation and dynamic element addition (`append`).
- Understand sequence generation logic with loop conditions.
- Implement robust exception handling for boundary inputs.
