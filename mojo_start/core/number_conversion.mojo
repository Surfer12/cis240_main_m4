# =========================================
# File: number_conversion.mojo
# Description:
#   1. Create a table listing powers of 2 (2^N down to 2^0).
#   2. Convert decimal <-> binary, decimal <-> hex.
#   3. Demo float -> IEEE 754 (single precision).
#   4. Show fraction handling hints for binary.
# =========================================

# -----------------------------------------
# 1. Power-of-2 Table Generation
# -----------------------------------------
fn create_power_table(decimal_value: Int, max_exponent: Int = 10) -> None:
    """
    Prints a Markdown-style table from 2^max_exponent down to 2^0,
    showing whether each power of 2 "fits" into `decimal_value`.

    Example for decimal_value=11, max_exponent=10:

    | Power (2^n) | Value | Does 11 fit? | Binary Bit |
    |---|---|---|---|
    | 2^10        | 1024 | No           | 0 |
    | 2^9         | 512  | No           | 0 |
    ...
    | 2^3         | 8    | Yes (leftover=3)  | 1 |
    | 2^2         | 4    | No (3 < 4)        | 0 |
    | 2^1         | 2    | Yes (leftover=1) | 1 |
    | 2^0         | 1    | Yes (leftover=0) | 1 |
    """
    print("| Power (2^n) | Value | Does {decimal_value} fit? | Binary Bit |")
    print("|---|---|---|---|")

    var remainder = decimal_value
    # Starting from 2^max_exponent down to 2^0
    for n in range(max_exponent, -1, -1):
        var power_value = 1 << n  # 2^n
        if power_value <= remainder:
            # That means it fits
            var remainder_str = "(leftover={})".format(remainder - power_value)
            print("| 2^{} | {} | Yes {} | 1 |".format(n, power_value, remainder_str))
            remainder -= power_value
        else:
            # Does not fit
            print("| 2^{} | {} | No            | 0 |".format(n, power_value))


# -----------------------------------------
# 3. Decimal <-> Hex
# -----------------------------------------
fn decimal_to_hex(decimal_value: Int) -> String:
    """
    Converts decimal integer to hexadecimal (without 0x prefix).
    """
    # You could also handle negatives by two's complement or just use built-in logic:
    return hex(decimal_value)[2:] if decimal_value >= 0 else "-" + hex(-decimal_value)[2:]

fn hex_to_decimal(hex_str: String) -> Int raises:
    """
    Converts a hexadecimal string (optionally with leading '-') back to decimal int.
    """
    # Detect a negative sign
    if hex_str.startswith('-'):
        return -int(hex_str[1:], 16)
    else:
        return int(hex_str, 16)


# -----------------------------------------
# (Optional) Handling Fractions in Binary
# -----------------------------------------
fn fraction_to_binary(fraction: f64, max_bits: Int = 8) -> String:
    """
    Converts the fractional part of a positive decimal number to binary up to `max_bits`.
    E.g., 0.25 -> "01" (since 0.25 = 2^-2).
    If fraction=0.25, you'd get '01' (meaning 0.01 in binary).
    """
    if fraction < 0:
        raise ValueError("Fraction must be non-negative for this function.")

    var bits = ""
    var value = fraction
    for _ in range(max_bits):
        value *= 2
        if value >= 1.0:
            bits += "1"
            value -= 1.0
        else:
            bits += "0"
        if value == 0:
            break
    return bits


# -----------------------------------------
# Demo main function
# -----------------------------------------
fn main():
    # 1. Print a table for integer part of, say, 11
    var demo_value = 11
    print("## Power-of-2 Table for {}".format(demo_value))
    create_power_table(demo_value, 10)
    print("")

    # 2. Show decimal -> binary -> decimal roundtrip
    var dec_val = -42
    var bin_rep = decimal_to_binary(dec_val, 16)
    var roundtrip_dec = binary_to_decimal(bin_rep)
    print("Decimal: {} -> Binary(16-bit): {} -> Back to Decimal: {}".format(dec_val, bin_rep, roundtrip_dec))
    print("")

    # 3. Show decimal -> hex -> decimal roundtrip
    var dec_hex_val = 255
    var hex_rep = decimal_to_hex(dec_hex_val)
    var roundtrip_hex_dec = hex_to_decimal(hex_rep)
    print("Decimal: {} -> Hex: {} -> Back to Decimal: {}".format(dec_hex_val, hex_rep, roundtrip_hex_dec))
    print("")

    # 4. Float -> IEEE 754 single -> float
    var fval = -123.456
    var f_ieee = float_to_ieee754_single(fval)
    var f_round = ieee754_single_to_float(f_ieee)
    print("Float value: {}".format(fval))
    print("IEEE754 single: {}".format(f_ieee))
    print("Converted back: {}".format(f_round))
    print("")

    # 5. Fractional part example (11.25)
    #    We'll show how to handle the 0.25 portion
    var fraction_part = 0.25
    var fraction_bits = fraction_to_binary(fraction_part, 8)
    # The integer part is 11 -> binary is 1011
    # The fraction part is 0.25 -> 0.01 in binary
    # Combined => 1011.01
    print("Example 11.25 => integer=11 (binary=1011) + fraction=0.25 (binary=0.{})".format(fraction_bits))
    print("So combined approx => 1011.{}".format(fraction_bits))
    print("")


main()