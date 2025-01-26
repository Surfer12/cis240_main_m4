fn dec_to_binary(decimal: Int) -> String:
    if decimal == 0:
        return "0"
    binary = ""
    is_negative = decimal < 0
    if is_negative:
        decimal = -decimal
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    if is_negative:
        binary = twos_complement(binary)
    return binary

fn twos_complement(binary: String) -> String:
    inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
    decimal_value = int(inverted_bits, 2) + 1
    return bin(decimal_value)[2:]

fn main():
    decimal_value = 42
    binary_representation = dec_to_binary(decimal_value)
    print(f"Binary representation of {decimal_value}: {binary_representation}")

main()