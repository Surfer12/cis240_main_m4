Below is a minimal Python example demonstrating two’s complement for integer values (step-by-step) and showing how you might obtain an IEEE 754 single-precision (32-bit) representation for floating-point values. These illustrate how negative numbers are actually handled at the hardware level, rather than relying on sign-magnitude strings.

Two’s Complement for Integers

The typical hardware process for a negative integer N in two’s complement form (assuming a fixed bit width) is:
	1.	Check if N is negative.
	2.	Convert the absolute value of N to binary.
	3.	Invert the bits.
	4.	Add 1 to form the final two’s complement result.

Below is a function that manually follows these steps for a chosen bit width. For simplicity, we’ll set a default of 8 bits, but you can pass in any bit width you need (e.g., 16, 32).

def int_to_twos_complement(num: int, bit_width: int = 8) -> str:
    """
    Return the two's complement representation of an integer `num`
    as a binary string, using `bit_width` bits.
    """
    # Range check (optional): in a real scenario you ensure
    # num is within -2^(bit_width-1) <= num < 2^(bit_width-1)
    max_pos = (1 << (bit_width - 1)) - 1
    min_neg = -(1 << (bit_width - 1))
    if not (min_neg <= num <= max_pos):
        raise ValueError(f"Number {num} is out of range for {bit_width}-bit two's complement.")

    # If non-negative, just format directly into binary
    if num >= 0:
        return format(num, f'0{bit_width}b')  # pad with zeros

    # For a negative number, do steps 2-4:
    abs_value = abs(num)

    # Step 2: Convert absolute value to binary (bit_width bits)
    positive_bits = format(abs_value, f'0{bit_width}b')

    # Step 3: Invert the bits (bitwise NOT)
    inverted_bits = ''.join('1' if bit == '0' else '0' for bit in positive_bits)

    # Step 4: Add 1
    # Easiest approach: convert inverted_bits to integer, add 1, then back to binary
    inverted_int = int(inverted_bits, 2)
    twos_comp_int = inverted_int + 1

    # Format again into a bit-width-limited binary
    twos_comp_bits = format(twos_comp_int, f'0{bit_width}b')

    return twos_comp_bits


# Example usage of int_to_twos_complement
if __name__ == "__main__":
    examples = [5, -5, 12, -12, 127, -128]  # within 8-bit range
    bit_width = 8

    for val in examples:
        binary_str = int_to_twos_complement(val, bit_width)
        print(f"{val} in {bit_width}-bit two's complement: {binary_str}")

Pythonic Shortcut for Two’s Complement

You may see a more compact trick in Python if you want a two’s complement representation:

def int_to_twos_complement_shortcut(num: int, bit_width: int) -> str:
    mask = (1 << bit_width) - 1  # e.g., for 8 bits, mask = 0xFF
    twos_comp_val = (num & mask)  # effectively applies two's complement
    return format(twos_comp_val, f'0{bit_width}b')

	•	This uses the fact that Python’s integers are unbounded, so using a bitwise AND with a mask ensures we “wrap” into the correct bit range in two’s complement form. However, the step-by-step version is more illustrative of how two’s complement works internally.

IEEE 754 (Single-Precision) for Floats

Floating-point values (e.g., -11.25) follow the IEEE 754 format at the hardware level, which is quite different from integer two’s complement. Here’s a simple example using Python’s struct module to display a float’s 32-bit representation:

import struct

def float_to_ieee754(num: float) -> str:
    """
    Convert a Python float to its 32-bit IEEE 754 representation.
    Returns the bits as a string of length 32.
    """
    # '>f' means: Big-endian, 4-byte float
    packed = struct.pack('>f', num)  # returns a bytes object of length 4
    # Convert each byte to 8 bits, then join them
    bits = ''.join(f'{byte:08b}' for byte in packed)
    return bits


if __name__ == "__main__":
    # Example float values
    float_examples = [3.5, -2.75, 0.0, 1.0, -0.1]

    for fval in float_examples:
        bits_32 = float_to_ieee754(fval)
        print(f"{fval:>6} in 32-bit IEEE 754: {bits_32}")

This approach packs the float according to the CPU’s standard single-precision layout (sign bit, exponent, significand).

	Note: IEEE 754 has separate sign, exponent, and mantissa (fraction) fields. This is quite distinct from integer two’s complement, so you can’t just invert-and-add-one to represent negative floats in IEEE 754.

Key Takeaways
	1.	Two’s Complement for Integers
	•	Negative integers are represented by inverting all bits of the absolute value and adding 1.
	•	This method keeps arithmetic consistent at the hardware level.
	2.	IEEE 754 for Floating-Point
	•	A separate sign bit, exponent field, and fraction field are stored.
	•	Negative floats don’t use two’s complement; they have a sign bit = 1, plus an exponent and fraction.
	3.	Machine-Level vs. Human-Readable
	•	A “-” sign in front of binary digits (like -1011.01) is human-readable but not how hardware typically stores negatives.
	•	For actual architecture courses and real CPUs, always remember two’s complement (for integers) and IEEE 754 (for floats).