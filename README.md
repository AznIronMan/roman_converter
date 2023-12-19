
# Roman Converter

## Overview
`roman_converter` is a Python package for converting between Roman numerals and integers. It provides functionality to convert integers to Roman numerals and vice versa. Additionally, it can parse numbers written in words and convert them to Roman numerals.

## Installation
```bash
pip install roman_converter
```

## Usage
You can use `roman_converter` in your Python code or as a command-line tool.

### In Python
Import the `convert_number` function from the package and use it as follows:

```python
from roman_converter import convert_number

# Convert an integer to Roman numeral
print(convert_number(31))  # Output: XXXI

# Convert a Roman numeral to an integer
print(convert_number('XXXI', to_roman=False, to_int=True))  # Output: 31

# Convert a number in words to Roman numeral
print(convert_number('thirty-one'))  # Output: XXXI
```

### Command-Line Interface
After installation, you can use `roman_converter` directly from the command line:

```bash
roman-converter 31
roman-converter --to_int XXXI
```

## License
This project is licensed under the MIT License.

## Author
Name:       Geoff Clark
Company:    ClarkTribeGames, LLC
Email:      geoff@clarktribegames.com
GitHub:     https://github.com/AznIronMan

## Contributions
Contributions are welcome! Please feel free to submit a pull request.
