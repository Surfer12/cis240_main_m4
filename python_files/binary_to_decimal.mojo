def binary_to_decimal(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num

binary_num = "101101"
decimal_num = binary_to_decimal(binary_num)
print(f"The decimal representation of {binary_num} is {decimal_num}")