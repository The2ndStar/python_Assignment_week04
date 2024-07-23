#7. Import functions from all three modules (`calculator` and `string_operations`) in `main.py`.
# main.py

from utilities.Calculator import add as add_def, subtarct as subtarct_def, multiply as multiply_def, divide as divide_def
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

print("Using calculator.py:")
print("Addition:", add_def(10, 5))
print("Subtraction:", subtarct_def(10, 5))
print("Multiplication:", multiply_def(10, 5))
print("Division:", divide_def(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))

