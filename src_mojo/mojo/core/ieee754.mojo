# =========================================
# File: ieee754.mojo
# Description:
#   Functions for converting float to IEEE 754 single precision.
# =========================================

# -----------------------------------------
# 1. Float -> IEEE 754 Single Precision
# -----------------------------------------
fn float_to_ieee754_single(value: Float) -> String:
    """
    Packs a 32-bit float into its IEEE 754 representation.
    NOTE: The 'struct' approach may vary depending on Mojo's runtime support.
    This is a demonstration approach using Python-like logic.
    """
    # In Mojo, you may or may not have the standard Python 'struct'.
    # For demonstration, we assume it's available or we replicate the logic.
    import struct
    packed = struct.pack('>f', value)                 # Big-endian float
    raw_int = struct.unpack('>I', packed)[0]          # Unpack as 32-bit int
    return format(raw_int, '032b')                    # Return as a 32-bit binary string

fn ieee754_single_to_float(ieee_binary: String) -> Float:
    """
    Converts a 32-bit binary string back to a float (IEEE 754 single).
    """
    import struct
    # Turn binary into int, then pack as big-endian unsigned int
    raw_int = int(ieee_binary, 2)
    packed = struct.pack('>I', raw_int)
    return struct.unpack('>f', packed)[0] 