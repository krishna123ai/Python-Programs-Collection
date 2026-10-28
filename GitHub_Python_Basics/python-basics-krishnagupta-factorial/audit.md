# Audit of README.md for factorial.py

This audit compares the claims in the initial generated README against the actual Python code in `factorial.py`.

## Claims Audit Table

| # | Claim in README | Status | Evidence from `factorial.py` | Action Taken |
|---|---|---|---|---|
| 1 | The program calculates the factorial of non-negative integers using an iterative loop. | **Supported** | Line 16: `for i in range(1, n + 1): result *= i` inside `calculate_factorial(n)`. | Kept in README. |
| 2 | The function raises `ValueError` for negative integer inputs. | **Supported** | Line 13-14: `if n < 0: raise ValueError(...)`. | Kept in README. |
| 3 | The function raises `TypeError` for non-integer inputs. | **Supported** | Line 11-12: `if not isinstance(n, int): raise TypeError(...)`. | Kept in README. |
| 4 | The script can be executed directly from terminal using `python factorial.py`. | **Supported** | Line 27-28: `if __name__ == "__main__": main()`. | Kept in README. |
| 5 | The program accepts user input dynamically via `input()` prompt from terminal. | **Not Supported** | Code uses fixed list `test_numbers = [0, 1, 5, 7, 10]` inside `main()`. There is no `input()` call. | Removed from README. |
| 6 | The program uses recursive memoization with caching. | **Not Supported** | No recursion, decorators, or memoization structures exist in the script; it uses a basic iterative `for` loop. | Removed from README. |
| 7 | The program requires external third-party math packages (e.g., `scipy` or `numpy`). | **Not Supported** | Only standard pure Python syntax is used without external packages. | Removed from README. |
| 8 | Learning objective: Understand integer loop multiplication and input validation in Python. | **Supported** | Reflected directly by the function structure and error assertions. | Kept in README. |

## Conclusion
Claims 5, 6, and 7 were found to be unsupported by the actual source code. The updated `README.md` has been modified to remove these claims and keep only verifiable features.
