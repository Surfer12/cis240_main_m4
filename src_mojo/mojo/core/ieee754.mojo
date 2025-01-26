# =========================================
# File: ieee754.mojo
# Description:
#   Functions for converting float to IEEE 754 single precision.
# =========================================

# -----------------------------------------
# 1. Float -> IEEE 754 Single Precision
# -----------------------------------------
from Python import import_module
struct = import_module("struct")

fn float_to_ieee754_single(value: Float) raises -> String:
    """
    Packs a 32-bit float into its IEEE 754 representation.
    NOTE: The 'struct' approach may vary depending on Mojo's runtime support.
    This is a demonstration approach using Python-like logic.
    """
    let pack_result = struct.invoke("pack", [">f", value])
    let raw_tuple = struct.invoke("unpack", [">I", pack_result])
    let raw_int = raw_tuple[0]
    return format(raw_int, "032b")

fn ieee754_single_to_float(ieee_binary: String) -> Float:
    """
    Converts a 32-bit binary string back to a float (IEEE 754 single).
    """
    import struct
    # Turn binary into int, then pack as big-endian unsigned int
    raw_int = int(ieee_binary, 2)
    packed = struct.pack('>I', raw_int)
    return struct.unpack('>f', packed)[0] 