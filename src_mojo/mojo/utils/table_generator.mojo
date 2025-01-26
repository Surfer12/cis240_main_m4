# =========================================
# File: table_generator.mojo
# Description:
#   Function for generating a power-of-2 table.
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

    remainder = decimal_value
    # Starting from 2^max_exponent down to 2^0
    for n in range(max_exponent, -1, -1):
        power_value = 1 << n  # 2^n
        if power_value <= remainder:
            # That means it fits
            remainder_str = f"(leftover={remainder - power_value})"
            print(f"| 2^{n} | {power_value} | Yes {remainder_str} | 1 |")
            remainder -= power_value
        else:
            # Does not fit
            print(f"| 2^{n} | {power_value} | No            | 0 |")

fn create_table() -> None:
    print("Creating table...")
    # Add your table creation logic here
    print("Table created successfully.")

fn main():
    create_table()

main()
