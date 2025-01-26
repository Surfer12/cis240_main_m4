def int_to_twos_complement_shortcut(num: int, bit_width: int) -> str:
    mask = (1 << bit_width) - 1  # e.g., for 8 bits, mask = 0xFF
    twos_comp_val = (num & mask)  # effectively applies two's complement
    return format(twos_comp_val, f'0{bit_width}b')
    