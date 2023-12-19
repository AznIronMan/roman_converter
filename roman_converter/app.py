import argparse
import re

from typing import Optional, Union
from word2number import w2n


def convert_number(
    input_value: Union[str, int],
    to_roman: Optional[bool] = None,
    to_int: Optional[bool] = None,
) -> Union[str, int]:
    if (to_roman == to_int) or (to_roman is None and to_int is None):
        if isinstance(input_value, int) or (
            isinstance(input_value, str) and input_value.isdigit()
        ):
            to_roman = True
            to_int = False
        elif isinstance(input_value, str):
            to_roman = False
            to_int = True
        else:
            raise ValueError(
                "Unable to determine conversion direction from input type."
            )
    if to_roman:
        if isinstance(input_value, str) and not input_value.isdigit():
            input_value = text_to_int(input_value)
        return int_to_roman(int(input_value))
    if to_int:
        return roman_to_int(str(input_value))
    raise ValueError("Invalid input type or conversion flags.")


def int_to_roman(num: int) -> str:
    if num <= 0:
        raise ValueError(
            "Roman numerals do not support zero or negative numbers"
        )
    if num > 3999:
        raise ValueError(
            "Number too large for standard Roman numeral representation"
        )
    val = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    parts = []
    for n, roman in val:
        (d, num) = divmod(num, n)
        parts.append(roman * d)
    return str("".join(parts))


def roman_to_int(s: str) -> int:
    valid_roman_regex = (
        r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    )
    s = s.upper()
    if not re.match(valid_roman_regex, s):
        raise ValueError("Invalid Roman numeral")
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "\u2160": 1,
        "\u2161": 2,
        "\u2162": 3,
        "\u2163": 4,
        "\u2164": 5,
        "\u2165": 6,
        "\u2166": 7,
        "\u2167": 8,
        "\u2168": 9,
        "\u2169": 10,
        "\u216A": 11,
        "\u216B": 12,
        "\u216C": 50,
        "\u216D": 100,
        "\u216E": 500,
        "\u216F": 1000,
        "\u2170": 1,
        "\u2171": 2,
        "\u2172": 3,
        "\u2173": 4,
        "\u2174": 5,
        "\u2175": 6,
        "\u2176": 7,
        "\u2177": 8,
        "\u2178": 9,
        "\u2179": 10,
        "\u217A": 11,
        "\u217B": 12,
        "\u217C": 50,
        "\u217D": 100,
        "\u217E": 500,
        "\u217F": 1000,
    }
    total = 0
    prev_value = 0
    for i in reversed(s):
        value = roman_dict.get(i, 0)
        if value == 0:
            raise ValueError("Invalid character in Roman numeral")
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return int(total)


def text_to_int(text: str) -> int:
    return int(w2n.word_to_num(text))


def text_to_roman(text: str) -> str:
    try:
        number = text_to_int(text)
        return int_to_roman(number)
    except Exception as e:
        return str(e)


def main():
    parser = argparse.ArgumentParser(
        description="Convert numbers to/from Roman numerals."
    )
    parser.add_argument("input_value", help="The value to convert.")
    parser.add_argument(
        "--to_roman", action="store_true", help="Convert to Roman numeral."
    )
    parser.add_argument(
        "--to_int", action="store_true", help="Convert to integer."
    )
    args = parser.parse_args()

    result = convert_number(
        args.input_value, to_roman=args.to_roman, to_int=args.to_int
    )
    print(result)


__all__ = ["convert_number"]

if __name__ == "__main__":
    main()
