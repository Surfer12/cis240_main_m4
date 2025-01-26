fn decimal_to_binary(decimal: Int) -> str:
    if decimal < 0:
        return to_twos_complement(decimal, 32)
    else:
        return bin(decimal)[2:]

fn main():
    decimal_value = -123
    binary_representation = decimal_to_binary(decimal_value)
    print(f"Binary representation of {decimal_value}: {binary_representation}") 