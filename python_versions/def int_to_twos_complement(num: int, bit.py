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