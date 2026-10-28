"""Struct-to-Dict Converter in Python.

This module demonstrates converting structured objects (custom class instances
and namedtuples) into standard Python dictionary representations.
"""

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class StudentRecord:
    """A structured representation of a student record."""

    roll_number: int
    name: str
    course: str
    grades: list[int]
    is_active: bool


def struct_to_dict(obj: Any) -> dict[str, Any]:
    """Convert a structured object or dataclass instance into a dictionary."""
    if hasattr(obj, "__dataclass_fields__"):
        return asdict(obj)
    if hasattr(obj, "_asdict"):
        return dict(obj._asdict())
    if hasattr(obj, "__dict__"):
        return dict(obj.__dict__)
    raise TypeError(f"Object of type {type(obj).__name__} is not convertible to dict.")


def main():
    print("--- Struct-to-Dict Program Demonstration ---")

    # Creating a sample structured object
    student = StudentRecord(
        roll_number=101,
        name="Krishna Gupta",
        course="Computer Science",
        grades=[85, 92, 78],
        is_active=True,
    )

    print("Original Structured Object:")
    print(student)

    # Conversion
    student_dict = struct_to_dict(student)

    print("\nConverted Dictionary:")
    print(student_dict)

    print("\nAccessing dictionary keys:")
    for key, value in student_dict.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")


if __name__ == "__main__":
    main()
