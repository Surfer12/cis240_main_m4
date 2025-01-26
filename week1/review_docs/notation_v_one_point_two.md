# Key Concepts and Insights: Number Base Notation

This document summarizes the key concepts related to number base notation, drawing from `notation_v_one.lua`. It incorporates LaTeX for mathematical expressions and code snippets to illustrate these concepts practically.

## 1. Positional Number Systems (Base Notation)

**Key Concept:** In a positional number system, the value of a digit depends on its position. Each position corresponds to a power of the base (radix).

**Mathematical Notation (LaTeX):**
A number $N$ in base $b$ can be represented as:

$$(d_m d_{m-1} \ldots d_1 d_0)_b$$

where $d_i$ is the digit at position $i$, and $0 \le d_i < b$.

**Polynomial Expansion:** The value of this number is given by the polynomial expansion:

$$N = \sum_{i=0}^{m} d_i \cdot b^i = d_m \cdot b^m + d_{m-1} \cdot b^{m-1} + \ldots + d_1 \cdot b^1 + d_0 \cdot b^0$$

**Example (LaTeX & Explanation):**
Consider the binary number $(1011)_2$.  Using the polynomial expansion with base $b=2$:

$$(1011)_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 8 + 0 + 2 + 1 = 11_{10}$$

Thus, $(1011)_2$ is equivalent to $11$ in decimal (base 10).

## 2. Common Number Bases and Symbol Sets

**Key Concept:** Different bases use different sets of symbols to represent digits.

| Base        | Name          | Symbols                                  |
|-------------|---------------|------------------------------------------|
| 2           | Binary        | 0, 1                                     |
| 8           | Octal         | 0, 1, 2, 3, 4, 5, 6, 7                     |
| 10          | Decimal       | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9                |
| 16          | Hexadecimal   | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F |

**Example (Hexadecimal - LaTeX & Explanation):**
In hexadecimal (base 16), the symbols A-F represent the decimal values 10-15 respectively. For example, $(2A)_{16}$:

$$(2A)_{16} = 2 \cdot 16^1 + A \cdot 16^0 = 2 \cdot 16 + 10 \cdot 1 = 32 + 10 = 42_{10}$$

Here, 'A' is interpreted as the decimal value 10.

## 3. Notation Conventions: Subscripts and Prefixes

**Key Concept:**  Subscripts and prefixes are used to explicitly denote the base of a number, especially in contexts where ambiguity might arise.

*   **Subscript Notation (LaTeX):**  $N_b$ indicates that $N$ is in base $b$.  Examples: $11_2$, $11_{10}$, $11_{16}$.

*   **Programming Prefixes (C-style):** Commonly used in programming languages to specify the base of literals:
    *   `0b` or `0B`: Binary (e.g., `0b1010`)
    *   `0`: Octal (e.g., `017`) - *Caution: Leading zero can be misinterpreted in decimal context if not careful.*
    *   No prefix: Typically implies decimal (e.g., `123`)
    *   `0x` or `0X`: Hexadecimal (e.g., `0xAF`)

**Mojo Code Example (Literals):**
Mojo, like many modern languages, supports these prefixes for number literals:

```mojo
fn main():
    let binary_num = 0b1011  # Binary literal
    let octal_num = 0o17     # Octal literal (using 0o prefix in Mojo, 0 in C-style)
    let decimal_num = 11     # Decimal literal (no prefix)
    let hex_num = 0x2A       # Hexadecimal literal

    print("Binary:", binary_num)
    print("Octal:", octal_num)
    print("Decimal:", decimal_num)
    print("Hexadecimal:", hex_num)
```

**Output:**
```
Binary: 11
Octal: 15
Decimal: 11
Hexadecimal: 42
```

**Explanation:** The Mojo code demonstrates how to directly represent numbers in different bases using prefixes. The output shows the decimal equivalent of each literal, confirming the base interpretation. Note that Mojo uses `0o` for octal prefix, which is more explicit than the C-style `0` prefix, reducing potential confusion.

## 4. Base Conversion: Decimal to Another Base

**Key Concept:** To convert a decimal number to another base, we use repeated division by the target base and collect the remainders.

**Algorithm (Decimal to Base $b$):**
1.  Divide the decimal number $N$ by the target base $b$.
2.  Record the remainder $r$. This is the least significant digit in base $b$.
3.  Replace $N$ with the quotient from the division.
4.  Repeat steps 1-3 until the quotient becomes 0.
5.  The digits in base $b$ are the remainders, read in reverse order of their calculation.

**Example (Decimal 26 to Hexadecimal - LaTeX & Explanation):**
Convert decimal 26 to hexadecimal (base 16):

1.  $26 \div 16 = 1$ with remainder $10$. Remainder $10$ in decimal is 'A' in hexadecimal.
2.  $1 \div 16 = 0$ with remainder $1$.

Reading the remainders in reverse order (1, then A), we get $(1A)_{16}$.

**Verification (Polynomial Expansion):**
$$(1A)_{16} = 1 \cdot 16^1 + A \cdot 16^0 = 1 \cdot 16 + 10 \cdot 1 = 26_{10}$$

## 5. Base Conversion: Another Base to Decimal

**Key Concept:** To convert a number from another base to decimal, use the polynomial expansion.

**Method (Base $b$ to Decimal):**
For a number $(d_m d_{m-1} \ldots d_1 d_0)_b$, the decimal value is:

$$N_{10} = \sum_{i=0}^{m} d_i \cdot b^i = d_m \cdot b^m + d_{m-1} \cdot b^{m-1} + \ldots + d_1 \cdot b^1 + d_0 \cdot b^0$$

**Example (Binary $(1011)_2$ to Decimal - LaTeX & Explanation):**
Convert binary $(1011)_2$ to decimal:

$$(1011)_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 8 + 0 + 2 + 1 = 11_{10}$$

## 6. Hexadecimal and Binary Relationship

**Key Insight:**  Each hexadecimal digit corresponds directly to 4 binary digits (bits). This simplifies conversions between hexadecimal and binary.

**Mapping (Hex Digit to 4 Bits):**

| Hex Digit | Binary (4 bits) | Hex Digit | Binary (4 bits) |
|-----------|-----------------|-----------|-----------------|
| 0         | 0000            | 8         | 1000            |
| 1         | 0001            | 9         | 1001            |
| 2         | 0010            | A         | 1010            |
| 3         | 0011            | B         | 1011            |
| 4         | 0100            | C         | 1100            |
| 5         | 0101            | D         | 1101            |
| 6         | 0110            | E         | 1110            |
| 7         | 0111            | F         | 1111            |

**Example (Hexadecimal $(2AF)_{16}$ to Binary - Explanation):**
To convert $(2AF)_{16}$ to binary, convert each hex digit to its 4-bit binary equivalent:

*   $2_{16} \rightarrow 0010_2$
*   $A_{16} \rightarrow 1010_2$
*   $F_{16} \rightarrow 1111_2$

Concatenating these binary groups gives: $(0010 \ 1010 \ 1111)_2$.  Leading zeros can be omitted for the most significant group, resulting in $(1010101111)_2$.

**Example (Binary $(110101)_2$ to Hexadecimal - Explanation):**
To convert $(110101)_2$ to hexadecimal:

1.  Group the binary digits into sets of 4, starting from the right. If needed, pad with leading zeros on the left to complete the leftmost group to 4 bits:  `0011 0101`.
2.  Convert each 4-bit group to its hexadecimal equivalent:
    *   $0011_2 \rightarrow 3_{16}$
    *   $0101_2 \rightarrow 5_{16}$

Concatenating the hexadecimal digits gives $(35)_{16}$.

## 7. Unsigned Numbers and Bit Representation

**Key Concept:** Computers represent numbers using a fixed number of bits. For $n$ bits, the range of unsigned integers is $0$ to $2^n - 1$.

**Example (32-bit Unsigned Integer - LaTeX):**
A 32-bit unsigned integer can represent values from 0 to $2^{32} - 1$.  The maximum value is:

$$2^{32} - 1 = 4,294,967,295$$

In hexadecimal, a 32-bit number is often represented using 8 hexadecimal digits (since $32 \div 4 = 8$). For example, a 32-bit binary number might be shown with leading zeros to explicitly indicate the 32-bit width.

## Conclusion

Understanding number base notation, conversion methods, and the relationship between binary and hexadecimal is fundamental in computer science. This document provides a concise reference with mathematical notation and practical code examples to solidify these concepts. By mastering these principles, you will be well-equipped to interpret and manipulate numerical data in various computing contexts.
```

