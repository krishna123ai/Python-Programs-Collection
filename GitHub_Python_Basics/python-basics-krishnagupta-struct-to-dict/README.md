# Struct-to-Dict Converter (Python Basics)

A beginner-friendly Python module demonstrating how to convert structured data models into standard Python dictionaries.

## What the Program Does
- Defines a structured data model `StudentRecord` using `@dataclass` with typed attributes: `roll_number`, `name`, `course`, `grades`, and `is_active`.
- Provides a conversion utility `struct_to_dict(obj)` that safely transforms structured objects (dataclasses, namedtuples, and standard class instances) into standard Python dictionaries (`dict`).
- Handles unsupported object types by raising a descriptive `TypeError`.
- Includes a runnable `main()` routine that instantiates a student record, performs the conversion, and displays key-value pairs along with their runtime data types.

## How to Run It
Execute the script using Python:
```bash
python struct-to-dict.py
```

### Sample Output
```
--- Struct-to-Dict Program Demonstration ---
Original Structured Object:
StudentRecord(roll_number=101, name='Krishna Gupta', course='Computer Science', grades=[85, 92, 78], is_active=True)

Converted Dictionary:
{'roll_number': 101, 'name': 'Krishna Gupta', 'course': 'Computer Science', 'grades': [85, 92, 78], 'is_active': True}

Accessing dictionary keys:
  roll_number: 101 (type: int)
  name: Krishna Gupta (type: str)
  course: Computer Science (type: str)
  grades: [85, 92, 78] (type: list)
  is_active: True (type: bool)
```

## Learning Objectives
- Understand structured object representations vs key-value dictionary mappings in Python.
- Utilize Python standard library tools (`dataclasses.asdict`).
- Implement duck typing and introspection (`hasattr`) for versatile type conversion.
