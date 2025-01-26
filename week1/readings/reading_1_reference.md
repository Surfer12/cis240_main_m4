# Reference Sheet for RISC-V Reading

## 2.2 Representing Numbers on Computers

### Key Concepts:

*   **Binary Addition:** Similar to decimal addition, but with only two digits (0 and 1). Carry digits are generated when the sum of digits in a column exceeds 1.
*   **Binary Subtraction:** Similar to decimal subtraction, but borrowing is required when subtracting a larger digit from a smaller one.

- "The concepts of binary addition and subtraction are fundamental to computer architecture. They are interconnected with topics like integer overflow and character encoding,"[text_link](binary-arithmetic-reflecton.md)



*   **Integer Overflow:** Occurs when the result of an arithmetic operation exceeds the maximum value that can be represented with a given number of bits.
    *   **Unsigned Overflow:** Occurs when adding two positive numbers results in a number too large to be represented.
    *   **Signed Overflow (Two's Complement):** Occurs when adding two numbers of the same sign results in a number with the opposite sign, exceeding the representable range.

### Figures:

*   **Figure 2.4:** Illustrates binary addition with and without carry indicators.
*   **Figure 2.5:** Demonstrates binary subtraction, highlighting the borrowing process.
*   **Figure 2.6:** Shows an example of unsigned integer overflow.
*   **Figure 2.7:** Shows an example of signed integer overflow in two's complement representation.

## 2.3 Representing Text

### Key Concepts:

*   **Character:** Basic unit of information in text representation (e.g., letters, digits, punctuation).
*   **Character Encoding Standard:** Defines how characters are represented as numbers on computers.
*   **ASCII (American Standard Code for Information Interchange):**
    *   7-bit encoding standard.
    *   Covers basic English characters and symbols.
    *   Limited support for other languages.
*   **Extended ASCII (EASCII):**
    *   An extension of ASCII.
    *   Includes more symbols but still limited.
*   **UTF-8 (Unicode Transformation Format - 8-bit):**
    *   Variable-width encoding (1-4 bytes per character).
    *   Most common encoding for web pages (over 95.5% as of 2020).
    *   Backward compatible with ASCII.
    *   Supports a wide range of characters from various languages.

### Table:

*   **Table 2.6:** Shows a subset of ASCII characters and their corresponding binary, hexadecimal, and decimal representations.
### Figures Reference Sheet:

| Figure Number | Description |
|---|---|
| Figure 2.4 | Adding two three-bit binary numbers. (a) Dashed arrows indicate where the carry out comes from. (b) Simplified representation (without arrows). |
| Figure 2.5 | Subtraction of two three-bit binary numbers. (a) The digits of both numbers are aligned on columns. (b) First, the least significant digits are subtracted - the “*” character indicates that some value was borrowed from the left column. (c) The second least significant digits are subtracted - again, the “*” character indicates that some value was borrowed from the left column. (d) Finally, the most significant digits are subtracted producing digit “0”. (e) Simplified representation of the subtraction. |
| Figure 2.6 | Example of an integer overflow on the unsigned binary representation. The result of one plus seven cannot be represented by a three-bit unsigned binary number. |
| Figure 2.7 | Example of an integer overflow on the signed binary representation. The result of three plus one cannot be represented by a three-bit signed binary number using the two’s complement representation. |
| Figure 2.8 | Word “ma¸c˜a” represented in three different character encoding standards: the UTF-8, the ISO-LATIN-1 and the Mac OS Roman |
| Table 2.6 | Subset of the characters encoded by the ASCII character encoding standard. Hex. and Dec. columns show the encoding value in hexadecimal and decimal representation while the Char. column shows the symbol encoded by the character. |