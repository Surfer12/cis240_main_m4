# Homework Practice

## Number Conversion

### Decimal to Binary

To convert a decimal number to binary, use the `decimal_to_binary` function in `src_mojo/mojo/conversions/number_conversion.mojo`.

```mojo
fn decimal_to_binary(decimal_value: Int, bit_length: Int = 32) -> String:
    if decimal_value >= 0:
        return format(decimal_value, "0" + str(bit_length) + "b")
    else:
        var positive_value = -decimal_value
        if positive_value >= (1 << bit_length):
            raise ValueError("Value too negative for the provided bit length.")
        let bin_pos = format(positive_value, "0" + str(bit_length) + "b")
        var inverted_bits = ""
        for bit in bin_pos:
            if bit == '0':
                inverted_bits = inverted_bits + '1'
            else:
                inverted_bits = inverted_bits + '0'
        let twos_comp_int = int(inverted_bits, base=2) + 1
        let twos_comp_str = format(twos_comp_int, "0" + str(bit_length) + "b")
        return twos_comp_str
```

### Binary to Decimal

To convert a binary number to decimal, use the `binary_to_decimal` function in `src_mojo/mojo/conversions/number_conversion.mojo`.

```mojo
fn binary_to_decimal(binary_str: String) -> Int raises:
    let bit_length = len(binary_str)
    if len(binary_str) == 0:
        raise ValueError("Empty binary string")

    if binary_str[0] == '0':
        return int(binary_str, base=2)
    else:
        var inverted_bits = ""
        for bit in binary_str:
            if bit == '1':
                inverted_bits = inverted_bits + '0'
            else:
                inverted_bits = inverted_bits + '1'
        var positive_part = int(inverted_bits, base=2) + 1
        return -positive_part
```

### IEEE 754 Single Precision

To convert a float to IEEE 754 single precision, use the `float_to_ieee754_single` function in `src_mojo/mojo/core/ieee754.mojo`.

```mojo
from Python import import_module
struct = import_module("struct")

fn float_to_ieee754_single(value: Float) raises -> String:
    let pack_result = struct.invoke("pack", [">f", value])
    let raw_tuple = struct.invoke("unpack", [">I", pack_result])
    let raw_int = raw_tuple[0]
    return format(raw_int, "032b")
```

By following these steps and adhering to the Mojo manual guidelines, you can ensure that your code is maintainable, readable, and adheres to best practices. This will help in the long run as your project evolves.

Hw practice 1: 

11.25 in base 10 to base 2 in binary

[text](<../../review_docs/Below is a step‐by‐step walkthrough of h.ini>)

<!-- [MermaidChart: c61e8022-b411-4a35-aa18-e706e1c013db] -->

<!-- [MermaidChart: 555e99db-f4a9-40a7-903b-bbbd29cd3f0d] -->


![alt text](<Screenshot 2025-01-26 at 07.22.03.png>)


Convert 43.125 ^ 10 to base 2 (binary)

I can see the integer part of translating would be 2^5 = 32 + 11.25 to get our 0 0 0 0 0 1 0 0 0 0 1 for 2^0 though 2 ^ 10 and then for the negatives it would be 0 0 1 0 0 for 2 ^-1 through 2^ -5

So the integer part of the number is 0 0 0 0 0 1 0 0 0 0 1 for 2^0 though 2 ^ 10 and then for the negatives it would be 0 0 1 0 0 for 2 ^-1 through 2^ -5


![alt text](<Screenshot 2025-01-26 at 06.45.27.png>)
![alt text](<Screenshot 2025-01-26 at 06.45.10.png>)


Convert 13.1875 ^ 10 to base 2 (binary)



Convert 4444.4444 ^ 10 to base 2 (binary)

Below [text](../lecture_1/lecture_1_problem_1.md)
Convert 0101 base 2 to base 10. 

0 \ 1 \ 0 \ 1 >

(0 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 0 + 4 + 0 + 1 = 5


Convert 0101.01 base 2 to base 10.

0 \ 1 \ 0 \ 1 \ . \ 0 \ 1 >

(0 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) + (0 * 2^-1) + (1 * 2^-2) = 0 + 4 + 0 + 1/4 + 0 + 0.25 = 5.25



`| Power | Value |` and `|---|---|`.
2. Iterate through the list of powers of 2
3. For each power, extract the exponent and the value.
4. Create a table row in markdown format: `| exponent | value |`.
5. Combine the header and rows to form the complete markdown table.
``` 
| Power | Value |
|---|---|
| 2^0 | 1 |
| 2^1 | 2 |
| 2^2 | 4 |
| 2^3 | 8 |
| 2^4 | 16 |
| 2^5 | 32 |
| 2^6 | 64 |
| 2^7 | 128 |
| 2^8 | 256 |
| 2^9 | 512 |
| 2^10 | 1024 |
```
