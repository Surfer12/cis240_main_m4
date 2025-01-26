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

def binary_to_decimal_float(binary_str: str) -> float:
    """Convert binary string to decimal, handling fractional parts."""
    if '.' not in binary_str:
        return float(binary_to_decimal(binary_str))
        
    int_part, frac_part = binary_str.split('.')
    
    # Convert integer part
    int_value = binary_to_decimal(int_part) if int_part else 0
    
    # Convert fractional part
    frac_value = 0.0
    for i, bit in enumerate(frac_part, 1):
        if bit == '1':
            frac_value += 2 ** -i
            
    return float(int_value) + frac_value

def show_binary_to_decimal_steps(binary_str: str) -> float:
    """Show step-by-step binary to decimal conversion."""
    print(f"\n=== Binary to Decimal Conversion Steps ===")
    print(f"Converting {binary_str} to decimal\n")
    
    # Split into integer and fractional parts
    parts = binary_str.split('.' if '.' in binary_str else '')
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ''
    
    # Integer part conversion
    is_negative = int_part and int_part[0] == '1'
    if is_negative:
        print("1. Number is negative (leftmost bit is 1)")
        print("2. Using two's complement for integer part:")
        print(f"   a. Original binary:     {int_part}")
        
        # Invert bits
        inverted = ''.join('1' if bit == '0' else '0' for bit in int_part)
        print(f"   b. Invert all bits:     {inverted}")
        
        # Add 1 and convert
        int_value = binary_to_decimal(int_part)
        print(f"   c. Add 1 and convert:   {int_value}")
    else:
        print("1. Integer part is positive (leftmost bit is 0)")
        int_value = binary_to_decimal(int_part)
        if int_part:
            print("2. Calculate integer powers of 2:")
            total = 0
            for i, bit in enumerate(reversed(int_part)):
                if bit == '1':
                    value = 1 << i
                    total += value
                    print(f"   2^{i} = {value}")
            print(f"\nInteger sum = {total}")
    
    # Fractional part conversion
    if frac_part:
        print("\n3. Convert fractional part:")
        print("   Calculate negative powers of 2:")
        frac_value = 0.0
        for i, bit in enumerate(frac_part, 1):
            if bit == '1':
                value = 2 ** -i
                frac_value += value
                print(f"   2^-{i} = {value}")
        print(f"\nFractional sum = {frac_value}")
        final_value = float(int_value) + frac_value
    else:
        final_value = float(int_value)
    
    print(f"\nFinal decimal value: {final_value}")
    return final_value

def to_ieee754(value: float) -> dict:
    """Convert a float to IEEE-754 single precision format."""
    import struct
    
    # Convert float to IEEE-754 binary representation
    binary = format(struct.unpack('!I', struct.pack('!f', value))[0], '032b')
    
    # Split into parts
    sign = binary[0]
    exponent = binary[1:9]
    mantissa = binary[9:]
    
    # Calculate components
    sign_value = int(sign)
    exponent_raw = int(exponent, 2)
    exponent_bias = exponent_raw - 127
    mantissa_value = 1 + sum(int(b) * 2**-i for i, b in enumerate(mantissa, 1))
    
    return {
        'binary': binary,
        'sign': sign,
        'exponent': exponent,
        'mantissa': mantissa,
        'sign_value': sign_value,
        'exponent_raw': exponent_raw,
        'exponent_bias': exponent_bias,
        'mantissa_value': mantissa_value
    }

def show_ieee754_visualization(value: float) -> None:
    """Show detailed IEEE-754 single precision representation."""
    print("\n=== IEEE-754 Single Precision Visualization ===")
    print(f"Converting {value} to IEEE-754 format\n")
    
    ieee = to_ieee754(value)
    
    # Show binary layout
    print("Binary layout (32 bits):")
    print("| Sign | Exponent | Mantissa |")
    print("|-------|-----------|-----------|")
    print(f"|   {ieee['sign']}   | {ieee['exponent']} | {ieee['mantissa']} |")
    
    # Show detailed breakdown
    print("\nComponent breakdown:")
    print(f"1. Sign bit: {ieee['sign']} ({'negative' if ieee['sign_value'] else 'positive'})")
    print(f"2. Exponent: {ieee['exponent']} (binary) = {ieee['exponent_raw']} (decimal)")
    print(f"   - Bias: 127")
    print(f"   - Actual exponent: {ieee['exponent_raw']} - 127 = {ieee['exponent_bias']}")
    print(f"3. Mantissa: 1.{ieee['mantissa']} = {ieee['mantissa_value']}")
    
    # Show final calculation
    print("\nFinal value calculation:")
    print(f"(-1)^{ieee['sign_value']} × {ieee['mantissa_value']} × 2^{ieee['exponent_bias']}")
    print(f"= {value}")

def group_bits(binary: str, group_size: int = 4) -> str:
    """Group binary digits for easier reading."""
    if '.' in binary:
        int_part, frac_part = binary.split('.')
        grouped_int = ' '.join(int_part[i:i+group_size] for i in range(0, len(int_part), group_size)).strip()
        grouped_frac = ' '.join(frac_part[i:i+group_size] for i in range(0, len(frac_part), group_size)).strip()
        return f"{grouped_int}.{grouped_frac}"
    return ' '.join(binary[i:i+group_size] for i in range(0, len(binary), group_size)).strip()

def show_bit_mapping(bin_str: str) -> None:
    """Show how bits map between different bases."""
    print("\nBit Mapping:")
    
    # Split into integer and fractional parts if needed
    parts = bin_str.split('.' if '.' in bin_str else '')
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ''
    
    # Pad integer part to multiple of 12 (LCM of 3 and 4 for octal and hex grouping)
    pad_len = (12 - len(int_part) % 12) % 12
    padded_bin = '0' * pad_len + int_part
    
    print("Binary groups (4 bits):")
    print(' '.join(padded_bin[i:i+4] for i in range(0, len(padded_bin), 4)))
    print("Hex digits:           ", end='')
    for i in range(0, len(padded_bin), 4):
        group = padded_bin[i:i+4]
        print(f"  {format(int(group, 2), 'X')}  ", end='')
    print("\n")
    
    print("Binary groups (3 bits):")
    print(' '.join(padded_bin[i:i+3] for i in range(0, len(padded_bin), 3)))
    print("Octal digits:         ", end='')
    for i in range(0, len(padded_bin), 3):
        group = padded_bin[i:i+3]
        print(f" {format(int(group, 2), 'o')} ", end='')
    print("\n")
    
    if frac_part:
        print("Fractional part mapping:")
        # Pad fractional part to multiple of 4 for hex grouping
        frac_pad = (4 - len(frac_part) % 4) % 4
        padded_frac = frac_part + '0' * frac_pad
        
        print("Binary groups:", ' '.join(padded_frac[i:i+4] for i in range(0, len(padded_frac), 4)))
        print("Hex digits:  ", end='')
        for i in range(0, len(padded_frac), 4):
            group = padded_frac[i:i+4]
            print(f"  {format(int(group, 2), 'X')}  ", end='')
        print()

def show_multi_base_layout(value: float) -> None:
    """Show the number in decimal, hexadecimal, binary, and octal formats."""
    print("\n=== Multi-Base Representation ===")
    
    # Handle integer and fractional parts separately
    int_part = int(value)
    frac_part = abs(value - int_part)
    
    # Format integer part in different bases
    hex_int = format(abs(int_part), 'X')
    oct_int = format(abs(int_part), 'o')
    bin_int = format(abs(int_part), 'b')
    
    # Format fractional part (if exists)
    if frac_part > 0:
        # Convert fraction to binary (up to 12 bits precision)
        bin_frac = ""
        frac = frac_part
        for _ in range(12):  # Increased precision for better octal conversion
            frac *= 2
            if frac >= 1:
                bin_frac += "1"
                frac -= 1
            else:
                bin_frac += "0"
        
        # Convert binary fraction to hex and octal
        hex_frac = ""
        for i in range(0, len(bin_frac), 4):
            chunk = bin_frac[i:i+4].ljust(4, '0')
            hex_digit = format(int(chunk, 2), 'X')
            hex_frac += hex_digit
            
        oct_frac = ""
        for i in range(0, len(bin_frac), 3):
            chunk = bin_frac[i:i+3].ljust(3, '0')
            oct_digit = format(int(chunk, 2), 'o')
            oct_frac += oct_digit
    
    # Create layout table
    print("\nNumber Layout:")
    print("┌─────────┬────────────────────────────────────────┐")
    print("│ Base    │ Representation                         │")
    print("├─────────┼────────────────────────────────────────┤")
    
    # Decimal (Base 10)
    print(f"│ Base 10 │ {value:<40} │")
    
    # Hexadecimal (Base 16)
    if frac_part > 0:
        hex_repr = f"{'-' if value < 0 else ''}0x{hex_int}.{hex_frac}"
    else:
        hex_repr = f"{'-' if value < 0 else ''}0x{hex_int}"
    print(f"│ Base 16 │ {hex_repr:<40} │")
    
    # Octal (Base 8)
    if frac_part > 0:
        oct_repr = f"{'-' if value < 0 else ''}0o{oct_int}.{oct_frac}"
    else:
        oct_repr = f"{'-' if value < 0 else ''}0o{oct_int}"
    print(f"│ Base 8  │ {oct_repr:<40} │")
    
    # Binary (Base 2)
    if frac_part > 0:
        bin_repr = f"{'-' if value < 0 else ''}0b{bin_int}.{bin_frac}"
    else:
        bin_repr = f"{'-' if value < 0 else ''}0b{bin_int}"
    print(f"│ Base 2  │ {group_bits(bin_repr[2:]):<40} │")
    print("└─────────┴────────────────────────────────────────┘")
    
    # Show bit patterns with grouping
    print("\nBit Patterns:")
    if frac_part > 0:
        print(f"Binary integer part:  {group_bits(bin_int)}")
        print(f"Binary fraction part: {group_bits(bin_frac)}")
    else:
        print(f"Binary pattern: {group_bits(bin_int)}")
    
    # Show bit mapping between bases
    show_bit_mapping(bin_int + ('.' + bin_frac if frac_part > 0 else ''))
    
    # Show conversion steps
    print("\nConversion Steps:")
    print("1. Decimal to Hexadecimal:")
    print(f"   {value} (base 10) = {hex_repr} (base 16)")
    print("2. Decimal to Octal:")
    print(f"   {value} (base 10) = {oct_repr} (base 8)")
    print("3. Decimal to Binary:")
    print(f"   {value} (base 10) = {bin_repr} (base 2)")
    if frac_part > 0:
        print("4. Fractional part conversion:")
        print(f"   0.{bin_frac} (binary) = {frac_part} (decimal)")

def main():
    while True:
        print("\n=== Number System Converter ===")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Show IEEE-754 Format")
        print("4. Show Multi-Base Layout")
        try:
            choice = input("Enter choice (1, 2, 3, or 4): ")
            
            if choice == "1":
                value = float(input("Enter decimal number: "))
                show_decimal_to_binary_steps(value)
                show_ieee754_visualization(value)
                show_multi_base_layout(value)
            elif choice == "2":
                value = input("Enter binary number: ")
                result = show_binary_to_decimal_steps(value)
                if '.' in value:  # Show IEEE-754 for fractional results
                    show_ieee754_visualization(result)
                show_multi_base_layout(float(result))
            elif choice == "3":
                value = float(input("Enter decimal number for IEEE-754 visualization: "))
                show_ieee754_visualization(value)
                show_multi_base_layout(value)
            else:
                value = float(input("Enter decimal number for multi-base visualization: "))
                show_multi_base_layout(value)
                
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