fn binary_to_decimal(binary: str) -> Int:
    if binary[0] == '1':  # Check if the number is negative (two's complement)
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
        decimal_value = int(inverted_bits, 2) + 1
        return -decimal_value
    else:
        return int(binary, 2)

fn main():
    binary_value = "11111111111111111111111110000101"
    decimal_representation = binary_to_decimal(binary_value)
    print(f"Decimal representation of {binary_value}: {decimal_representation}")