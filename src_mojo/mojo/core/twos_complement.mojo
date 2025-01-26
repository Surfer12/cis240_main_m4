# =========================================
# File: twos_complement.mojo
# Description:
#   Functions for converting between decimal and binary using two's complement.
# =========================================

# -----------------------------------------
# 1. Decimal <-> Binary (with two's complement for negatives)
# -----------------------------------------
fn decimal_to_binary(decimal_value: Int, bit_length: Int = 32) -> String:
    """
    Converts an integer to its binary representation, using
    two's complement if it's negative, restricted to `bit_length` bits.
    """
    if decimal_value >= 0:
        # Positive or zero: just format it
        return format(decimal_value, f'0{bit_length}b')
    else:
        # Negative: compute two's complement within bit_length
        positive_value = -decimal_value
        if positive_value >= (1 << bit_length):
            raise ValueError("Value too negative for the provided bit length.")
        # Format as binary
        bin_pos = format(positive_value, f'0{bit_length}b')
        # Invert bits
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in bin_pos)
        # Add 1
        twos_comp_int = int(inverted_bits, 2) + 1
        # Convert back to binary string
        twos_comp_str = format(twos_comp_int, f'0{bit_length}b')
        return twos_comp_str

fn binary_to_decimal(binary_str: String) -> Int raises:
    """
    Converts a binary string to its decimal representation.
    Interprets two's complement if the leftmost bit is 1.
    """
    let bit_length = len(binary_str)
    if len(binary_str) == 0:
        raise ValueError("Empty binary string")

    if binary_str[0] == '0':
        return int(binary_str, base=2)
    else:
        var inverted_bits = ""
        for bit in binary_str:
            if bit == '1':
                inverted_bits = inverted_bits + '0'
            else:
                inverted_bits = inverted_bits + '1'
        var positive_part = int(inverted_bits, base=2) + 1
        return -positive_part