# =========================================
# File: number_conversion_interactive.py
# Description:
#   Interactive utility for number system conversions
#   with step-by-step visualization.
# =========================================

def create_power_table(decimal_value: float, max_exponent: int = 10, show_fractional: bool = False) -> None:
    """
    Prints a table showing powers of 2 and whether they fit in decimal_value.
    """
    int_part = int(decimal_value)
    if show_fractional:
        print("| Power (2^n) | Value      | Does {} fit? | Binary Bit |".format(decimal_value))
    else:
        print("| Power (2^n) | Value      | Does {} fit? | Binary Bit |".format(int_part))
    print("|-------------|------------|--------------|------------|")

    remainder = int_part
    for n in range(max_exponent, -1, -1):
        power_value = 1 << n  # 2^n
        if power_value <= remainder:
            remainder_str = f"(leftover={remainder - power_value})"
            print(f"| 2^{n:<9} | {power_value:<10} | Yes {remainder_str:<8} | 1          |")
            remainder -= power_value
        else:
            print(f"| 2^{n:<9} | {power_value:<10} | No           | 0          |")

def create_fractional_power_table(fractional_part: float, precision: int = 4) -> None:
    """
    Prints a table showing negative powers of 2 for fractional part.
    """
    print("\nFractional part powers:")
    print("| Power (2^-n) | Value      | Does {} fit? | Binary Bit |".format(fractional_part))
    print("|--------------|------------|--------------|------------|")

    remainder = fractional_part
    for n in range(1, precision + 1):
        power_value = 2 ** -n
        if power_value <= remainder:
            remainder_str = f"(leftover={remainder - power_value:.6f})"
            print(f"| 2^-{n:<8} | {power_value:<10.6f} | Yes {remainder_str:<8} | 1          |")
            remainder -= power_value
        else:
            print(f"| 2^-{n:<8} | {power_value:<10.6f} | No           | 0          |")

def decimal_to_binary_float(decimal_value: float, int_bits: int = 32, frac_bits: int = 4) -> str:
    """Convert decimal (including fractional) to binary string."""
    int_part = int(decimal_value)
    frac_part = abs(decimal_value - int_part)
    
    # Convert integer part
    if int_part >= 0:
        int_str = format(int_part, f'0{int_bits}b')
    else:
        # Handle negative numbers using two's complement
        max_val = (1 << int_bits)
        int_str = format((max_val + int_part) & (max_val - 1), f'0{int_bits}b')
    
    # Convert fractional part
    if frac_part == 0:
        return int_str
    
    frac_str = ""
    for _ in range(frac_bits):
        frac_part *= 2
        if frac_part >= 1:
            frac_str += "1"
            frac_part -= 1
        else:
            frac_str += "0"
    
    return f"{int_str}.{frac_str}"

def show_decimal_to_binary_steps(decimal_value: float, int_bits: int = 32, frac_bits: int = 4) -> str:
    """Show step-by-step decimal to binary conversion."""
    print(f"\n=== Decimal to Binary Conversion Steps ===")
    print(f"Converting {decimal_value} to binary\n")
    
    int_part = int(decimal_value)
    frac_part = abs(decimal_value - int_part)
    
    is_negative = decimal_value < 0
    abs_value = abs(int_part)
    
    # Integer part conversion
    if is_negative:
        print(f"1. Take absolute value: |{decimal_value}| = {abs(decimal_value)}")
        print(f"2. Split into integer and fractional parts:")
        print(f"   Integer part: {abs_value}")
        print(f"   Fractional part: {frac_part}")
        print("\n3. Convert absolute integer part to binary:")
    else:
        print(f"1. Split into integer and fractional parts:")
        print(f"   Integer part: {int_part}")
        print(f"   Fractional part: {frac_part}")
        print("\n2. Convert integer part to binary:")
    
    create_power_table(abs_value, int_bits-1)
    
    # Fractional part conversion
    if frac_part > 0:
        print("\n3. Convert fractional part to binary:")
        create_fractional_power_table(frac_part, frac_bits)
    
    # Get final binary representation
    bin_str = decimal_to_binary_float(decimal_value, int_bits, frac_bits)
    print(f"\nFinal binary: {bin_str}")
    return bin_str

def binary_to_decimal(binary_str: str) -> int:
    """Convert binary string to decimal, handling two's complement for negative numbers."""
    if binary_str[0] == '0':
        return int(binary_str, 2)
    else:
        # Handle negative numbers in two's complement
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        return -(int(inverted, 2) + 1)

def show_binary_to_decimal_steps(binary_str: str) -> int:
    """Show step-by-step binary to decimal conversion."""
    print(f"\n=== Binary to Decimal Conversion Steps ===")
    print(f"Converting {binary_str} to decimal\n")
    
    is_negative = binary_str[0] == '1'
    if is_negative:
        print("1. Number is negative (leftmost bit is 1)")
        print("2. Using two's complement to convert:")
        print(f"   a. Original binary:     {binary_str}")
        
        # Invert bits
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        print(f"   b. Invert all bits:     {inverted}")
        
        # Add 1 and convert
        decimal_val = binary_to_decimal(binary_str)
        print(f"   c. Add 1 and convert:   {decimal_val}")
    else:
        print("1. Number is positive (leftmost bit is 0)")
        decimal_val = binary_to_decimal(binary_str)
        
        # Show power calculation
        print("2. Calculate powers of 2:")
        total = 0
        for i, bit in enumerate(reversed(binary_str)):
            if bit == '1':
                value = 1 << i
                total += value
                print(f"   2^{i} = {value}")
        print(f"\nSum of powers = {total}")
    
    print(f"\nFinal decimal value: {decimal_val}")
    return decimal_val

def main():
    while True:
        print("\n=== Number System Converter ===")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        try:
            choice = input("Enter choice (1 or 2): ")
            
            if choice == "1":
                value = float(input("Enter decimal number: "))
                show_decimal_to_binary_steps(value)
            else:
                value = input("Enter binary number: ")
                show_binary_to_decimal_steps(value)
                
            again = input("\nConvert another number? (y/n): ").lower()
            if again != 'y':
                break
                
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
            continue
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main() 