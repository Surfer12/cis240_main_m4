fn decimal_to_binary(decimal_num: F64) -> String:
    // Handle the integer part
    integer_part = int(decimal_num)
    binary_integer = ""
    while integer_part > 0:
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part = integer_part // 2

    // Handle the fractional part
    fractional_part = decimal_num - int(decimal_num)
    binary_fractional = ""
    while fractional_part > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit

    // Combine integer and fractional parts
    binary_num = binary_integer + "." + binary_fractional
    return binary_num

fn main():
    decimal_num = 11.25
    binary_num = decimal_to_binary(decimal_num)
    print(f"The binary representation of {decimal_num} is {binary_num}")

main()