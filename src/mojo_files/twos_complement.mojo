fn to_twos_complement(value: Int, bit_length: Int) -> str:
    if value >= 0:
        return format(value, f'0{bit_length}b')
    else:
        positive_value = abs(value)
        binary_representation = format(positive_value, f'0{bit_length}b')
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
        twos_complement = bin(int(inverted_bits, 2) + 1)[2:].zfill(bit_length)
        return twos_complement 