def decimal_to_binary(decimal_num):
    """
    Converts a decimal number (integer or float) to its binary representation (as a string).
    """
    if not isinstance(decimal_num, (int, float)):
        raise ValueError("Input must be an integer or a float.")

    # Separate integer and fractional parts
    integer_part = int(decimal_num)
    binary_integer = bin(integer_part).replace("0b", "")

    # Check sign of the original value
    is_negative = (decimal_num < 0)
    if is_negative:
        # Convert the absolute value to binary
        integer_part = abs(integer_part)
        binary_integer = bin(integer_part).replace("0b", "")

    # Handle the fractional part
    fractional_part = abs(decimal_num) - abs(integer_part)
    binary_fractional = ""
    while fractional_part != 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
        if len(binary_fractional) > 32:  # Stop early to avoid infinite loop on non-terminating fractions
            break

    # Combine integer and fractional parts
    if binary_fractional:
        binary_string = f"{binary_integer}.{binary_fractional}"
    else:
        binary_string = binary_integer

    # Prefix negative sign if needed
    if is_negative:
        binary_string = "-" + binary_string

    return binary_string


def binary_to_decimal(binary_num):
    """
    Converts a binary number (string) to its decimal representation (float).
    """
    if not isinstance(binary_num, str):
        raise ValueError("Input must be a string.")

    # Check sign of the original value
    is_negative = binary_num.startswith("-")
    if is_negative:
        binary_num = binary_num[1:]  # Strip the negative sign for processing

    # Separate integer and fractional parts
    if '.' in binary_num:
        integer_part, fractional_part = binary_num.split('.')
    else:
        integer_part, fractional_part = binary_num, ''

    # Convert integer part
    decimal_integer = int(integer_part, 2) if integer_part else 0

    # Convert fractional part
    decimal_fractional = 0.0
    for i, bit in enumerate(fractional_part, start=1):
        decimal_fractional += int(bit) * (2 ** -i)

    # Combine and reapply sign
    decimal_value = decimal_integer + decimal_fractional
    if is_negative:
        decimal_value = -decimal_value

    return decimal_value


# Example data for demonstrating table output
decimal_values = [11, 11.25, -11.25, 0, 5.5, 2]
binary_values = ["1011", "1011.01", "-1011.01", "0", "101", "10.1"]


# Print decimal-to-binary conversion table
print("Decimal to Binary Conversion Table")
print("----------------------------------")
print(f"{'Decimal':<15} | {'Binary':<20}")
print("-" * 36)
for dec in decimal_values:
    bin_rep = decimal_to_binary(dec)
    print(f"{dec:<15} | {bin_rep:<20}")

print("\nBinary to Decimal Conversion Table")
print("----------------------------------")
print(f"{'Binary':<15} | {'Decimal':<20}")
print("-" * 36)
for bin_val in binary_values:
    dec_rep = binary_to_decimal(bin_val)
    print(f"{bin_val:<15} | {dec_rep:<20}")