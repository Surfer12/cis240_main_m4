fn float_to_ieee754(value: Float) -> str:
    import struct
    packed = struct.pack('>f', value)
    hex_representation = hex(struct.unpack('>I', packed)[0])[2:].zfill(8)
    return hex_representation 