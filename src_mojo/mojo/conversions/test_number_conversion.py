import unittest
from number_conversion_interactive import (
    decimal_to_binary_float,
    binary_to_decimal_float,
    to_base32,
    perform_binary_arithmetic,
    parse_number,
    group_bits,
    color_binary_groups
)
from signed_representations import check_overflow
from circuit_visualization import show_half_adder, show_full_adder

class TestNumberConversion(unittest.TestCase):
    """Test suite for number conversion utility."""
    
    def test_decimal_to_binary(self):
        """Test decimal to binary conversion."""
        test_cases = [
            (42, "00000000000000000000000000101010"),
            (0, "00000000000000000000000000000000"),
            (-42, "11111111111111111111111111010110"),
            (255, "00000000000000000000000011111111"),
            (3.75, "00000000000000000000000000000011.1100"),
            (-3.75, "11111111111111111111111111111101.1100"),
        ]
        
        for decimal, expected in test_cases:
            with self.subTest(decimal=decimal):
                result = decimal_to_binary_float(decimal)
                self.assertEqual(result, expected)
    
    def test_binary_to_decimal(self):
        """Test binary to decimal conversion."""
        test_cases = [
            ("00101010", 42),      # Add leading zeros to indicate unsigned
            ("00000000", 0),
            ("11111111", 255),     # Unsigned 8-bit
            ("00000011.11", 3.75), # Add leading zeros for positive
            ("1111111111111111", 65535),  # 16-bit unsigned
        ]
        
        for binary, expected in test_cases:
            with self.subTest(binary=binary):
                result = binary_to_decimal_float(binary)
                self.assertEqual(result, expected)
    
    def test_binary_arithmetic(self):
        """Test binary arithmetic operations."""
        # Addition
        a, b = format(5, 'b'), format(3, 'b')  # 5 + 3
        result, _ = perform_binary_arithmetic(a, b, 'add')
        self.assertEqual(int(result, 2), 8)
        
        # Subtraction
        a, b = format(8, 'b'), format(3, 'b')  # 8 - 3
        result, _ = perform_binary_arithmetic(a, b, 'subtract')
        self.assertEqual(int(result, 2), 5)
        
        # Multiplication
        a, b = format(5, 'b'), format(3, 'b')  # 5 * 3
        result, _ = perform_binary_arithmetic(a, b, 'multiply')
        self.assertEqual(int(result, 2), 15)
        
        # Division
        a, b = format(15, 'b'), format(3, 'b')  # 15 ÷ 3
        result, _ = perform_binary_arithmetic(a, b, 'divide')
        self.assertEqual(int(result, 2), 5)
    
    def test_overflow_detection(self):
        """Test overflow detection in arithmetic operations."""
        # 4-bit overflow cases
        bits = 4
        max_val = (1 << (bits - 1)) - 1  # 7 for 4 bits
        min_val = -(1 << (bits - 1))     # -8 for 4 bits
        
        # Addition overflow
        has_overflow, _ = check_overflow(max_val, 1, max_val + 1, bits, 'add')
        self.assertTrue(has_overflow)
        
        # Subtraction overflow
        has_overflow, _ = check_overflow(min_val, 1, min_val - 1, bits, 'subtract')
        self.assertTrue(has_overflow)
        
        # Multiplication overflow
        has_overflow, _ = check_overflow(max_val, 2, max_val * 2, bits, 'multiply')
        self.assertTrue(has_overflow)
        
        # No overflow case
        has_overflow, _ = check_overflow(1, 1, 2, bits, 'add')
        self.assertFalse(has_overflow)
    
    def test_base32_conversion(self):
        """Test base32 conversion."""
        test_cases = [
            (42, "BK"),
            (255, "H7"),
            (1024, "BAA"),
            (3.75, "D.Y"),
        ]
        
        for decimal, expected in test_cases:
            with self.subTest(decimal=decimal):
                result = to_base32(decimal)
                self.assertEqual(result, expected)
    
    def test_number_parsing(self):
        """Test number parsing in different bases."""
        test_cases = [
            ("42", 10, 42),
            ("0b101010", 2, 42),
            ("0x2A", 16, 42),
            ("0o52", 8, 42),
        ]
        
        for number_str, base, expected in test_cases:
            with self.subTest(number=number_str, base=base):
                result = parse_number(number_str, base)
                self.assertEqual(result, expected)
    
    def test_bit_grouping(self):
        """Test binary digit grouping."""
        test_cases = [
            ("1010", 2, "10 10"),
            ("1111", 4, "1111"),
            ("101010", 3, "101 010"),
            ("1010.1010", 2, "10 10.10 10"),
        ]
        
        for binary, group_size, expected in test_cases:
            with self.subTest(binary=binary, group_size=group_size):
                result = group_bits(binary, group_size)
                self.assertEqual(result, expected)
    
    def test_color_grouping(self):
        """Test color-coded binary grouping."""
        # Note: This test only checks if the function runs without errors
        # since testing ANSI color codes in strings is complex
        test_cases = ["1010", "1111", "101010", "1010.1010"]
        
        for binary in test_cases:
            with self.subTest(binary=binary):
                result = color_binary_groups(binary)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), len(binary))

def run_tests():
    """Run all tests with detailed output."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumberConversion)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests() 