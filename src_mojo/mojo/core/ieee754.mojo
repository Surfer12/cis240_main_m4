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
    Converts a float to its IEEE 754 single precision binary representation.
    """
    let pack_result = struct.invoke("pack", [">f", value])
    let raw_tuple = struct.invoke("unpack", [">I", pack_result])
    let raw_int = raw_tuple[0]
    return format(raw_int, "032b")

fn ieee754_single_to_float(ieee_binary: String) raises -> Float:
    """
    Converts a 32-bit binary string back to a float (IEEE 754 single).
    """
    let raw_int = int(ieee_binary, base=2)
    let pack_bytes = struct.invoke("pack", [">I", raw_int])
    let float_tuple = struct.invoke("unpack", [">f", pack_bytes])
    return float_tuple[0] 