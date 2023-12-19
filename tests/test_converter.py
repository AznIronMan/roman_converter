import unittest
from roman_converter.app import convert_number as roman_converter


class TestRomanConverter(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual(
            roman_converter(31, to_roman=True, to_int=False), "XXXI"
        )

    def test_roman_to_int(self):
        self.assertEqual(
            roman_converter("XXXI", to_roman=False, to_int=True), 31
        )

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            roman_converter("invalid", to_roman=False, to_int=True)


if __name__ == "__main__":
    unittest.main()
