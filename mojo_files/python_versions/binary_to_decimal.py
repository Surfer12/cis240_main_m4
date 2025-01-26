def binary_to_decimal(binary_num):
    if not isinstance(binary_num, str):
        raise ValueError("Input must be a string")

    # Split the binary number into integer and fractional parts
    if '.' in binary_num:
        integer_part, fractional_part = binary_num.split('.')
    else:
        integer_part, fractional_part = binary_num, ''

    # Convert the integer part
    decimal_integer = int(integer_part, 2)

    # Convert the fractional part
    decimal_fractional = 0
    for i, bit in enumerate(fractional_part):
        decimal_fractional += int(bit) * (2 ** -(i + 1))

    # Combine integer and fractional parts
    decimal_num = decimal_integer + decimal_fractional

    return decimal_num

# Test with an integer binary
binary_num = "1011"
decimal_num = binary_to_decimal(binary_num)
print(f"The decimal representation of {binary_num} is {decimal_num}")

# Test with a float binary
binary_num = "1011.01"
decimal_num = binary_to_decimal(binary_num)
print(f"The decimal representation of {binary_num} is {decimal_num}")

# Test with a negative float binary
binary_num = "-1011.01"
decimal_num = binary_to_decimal(binary_num)
print(f"The decimal representation of {binary_num} is {decimal_num}")