def create_conversion_table(decimal_num):
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

    # Create the table
    table = f"Conversion Table for {decimal_num}\n"
    table += "=" * 30 + "\n"
    table += f"Decimal: {decimal_num}\n"
    table += f"Binary: {binary_num}\n"
    table += "-" * 30 + "\n"

    # Integer part table
    table += "Integer Part Conversion\n"
    table += "Step | Quotient | Remainder\n"
    table += "-" * 30 + "\n"
    quotient = integer_part
    step = 1
    while quotient > 0:
        remainder = quotient % 2
        quotient //= 2
        table += f"{step} | {quotient} | {remainder}\n"
        step += 1

    # Fractional part table
    table += "\nFractional Part Conversion\n"
    table += "Step | Fractional Part | Multiplied by 2 | Bit | Remainder\n"
    table += "-" * 60 + "\n"
    fractional_part = decimal_num - integer_part
    step = 1
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_part -= bit
        table += f"{step} | {fractional_part + bit} | {fractional_part + bit * 2} | {bit} | {fractional_part}\n"
        step += 1
        if step > 32:  # Prevent infinite loop for non-terminating decimals
            break

    return table

# Test with a float
decimal_num = 11.25
table = create_conversion_table(decimal_num)
print(table)