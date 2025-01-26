import struct

def float_to_ieee754(num: float) -> str:
    """
    Convert a Python float to its 32-bit IEEE 754 representation.
    Returns the bits as a string of length 32.
    """
    # '>f' means: Big-endian, 4-byte float
    packed = struct.pack('>f', num)  # returns a bytes object of length 4
    # Convert each byte to 8 bits, then join them
    bits = ''.join(f'{byte:08b}' for byte in packed)
    return bits


if __name__ == "__main__":
    # Example float values
    float_examples = [3.5, -2.75, 0.0, 1.0, -0.1]

    for fval in float_examples:
        bits_32 = float_to_ieee754(fval)
        print(f"{fval:>6} in 32-bit IEEE 754: {bits_32}")