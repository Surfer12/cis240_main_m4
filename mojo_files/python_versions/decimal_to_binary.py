def decimal_to_binary(decimal_num):
    if not isinstance(decimal_num, (int, float)):
        raise ValueError("Input must be an integer or a float")

    # Handle the integer part
    integer_part = int(decimal_num)
    binary_integer = bin(integer_part).replace("0b", "")

    # Handle the fractional part
    fractional_part = decimal_num - integer_part
    binary_fractional = ""
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
        if len(binary_fractional) > 32:  # Prevent infinite loop for non-terminating decimals
            break

    # Combine integer and fractional parts
    if binary_fractional:
        binary_num = f"{binary_integer}.{binary_fractional}"
    else:
        binary_num = binary_integer

    return binary_num

# Test with an integer
decimal_num = 11
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")

# Test with a float
decimal_num = 11.25
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")

# Test with a negative float
decimal_num = -11.25
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")