# Week 1 Notation Guide: Number Bases and Conversions

This guide clarifies the mathematical notation and concepts related to number bases and conversions, as covered in Week 1 materials. Understanding this notation is essential for working with different number systems in computer architecture.

## 1. Base/Positional Notation Basics

**Key Concept:** In a base-$b$ system, a number is represented as a sequence of digits, where each digit's position determines its contribution to the number's value, weighted by powers of the base $b$.

**Notation:**
 -  $ (d_n d_{n-1} ... d_1 d_0)_b $ denotes a number in base $b$.
 - Digits in base $b$ are represented as $d_i$, where $0 \leq d_i < b$.
 - **Example:** $ (1011)_2 $ in binary means:
   $ 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 $

## 2. Polynomial Representation (Equations 2.4/2.5)

**Equation 2.4 (General Base):**

$$ Value = \sum_{i=0}^{n} d_i \times b^i $$

 - $ d_i $ is the digit in the $i$-th position (from the right, starting at position 0).
 - $ \text{value}(d_i) $ is the integer value of the digit symbol.
 - $ i $ ranges from 0 to $n$. For base 2, digits are 0 or 1; for base 16, digits are 0-9, A-F.

**Equation 2.5 (Base 2 Specific):**

$$ Value = \sum_{i=0}^{n} d_i \times 2^i $$

 - **Interpretation:** Numbers are polynomials in base $b$. Each digit is a coefficient of a power of $b$.

## 3. Symbol Sets for Common Bases (Table 2.1)

 - **Binary (Base 2):** 0, 1.
 - **Octal (Base 8):** 0, 1, 2, 3, 4, 5, 6, 7.
 - **Decimal (Base 10):** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
 - **Hexadecimal (Base 16):** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F (A=10, B=11, C=12, D=13, E=14, F=15).

**Examples:**
 - $ (26)_{10} $ in decimal is $ (1A)_{16} $ in hexadecimal.
 - $ (1010)_2 $ in binary is $ (10)_{10} $ in decimal.

## 4. Subscripts, Prefixes, and Suffixes

 - **Subscript Notation:**
   - $ 11_2 $ means "the number 11 in base 2".
   - $ 11_{10} $ means "the number 11 in base 10".
   - $ 11_{16} $ means "the number 11 in base 16".
 - **Programming Language Prefixes (e.g., C):**
   - `0b1010` (binary)
   - `010` (octal)
   - `0x10` (hexadecimal)
   - No prefix typically implies decimal.

## 5. Converting Between Bases (Equations 2.6, 2.7, etc.)

 - **General Methods:**
   - **Decimal to Another Base:** Repeatedly divide the decimal number by the new base $b$, record remainders, and read digits in reverse order.
   - **Another Base to Decimal:** Expand the number as a polynomial (Equation 2.4) or sum up digit × base<sup>position</sup>.

 - **Example: Converting 26 to hexadecimal (Algorithm 2 example):**
   1. $ 26 \div 16 = 1 $ with remainder $ 10 $ (remainder "10" in decimal is "A" in hex).
   2. $ 1 \div 16 = 0 $ with remainder $ 1 $ (digit "1").
   - Reading remainders from last to first: $ (1A)_{16} $.

 - **Equation 2.8:** Each hexadecimal digit maps to 4 bits in binary and vice versa, simplifying conversions between these bases.
 - **Equation 2.9:** Example of a large binary number $ (1011\ 0100\ 1001)_2 $ represented in hexadecimal as $ (B49)_{16} $, showing direct nibble-to-hex-digit translation.

## 6. Unsigned Numbers on Computers

 - With $ n $ bits, the representable range for unsigned numbers is $ 0 $ to $ 2^n - 1 $ (e.g., 8 bits: 0 to 255).
 - **Equation 2.10:** Example of $ (255)_{10} $ as $ (11111111)_2 $ in 8 bits.
 - **Equation 2.11:** Example of $ (4294967295)_{10} $ as $ (FFFFFFFF)_{16} $ or $ (11111111\ 11111111\ 11111111\ 11111111)_2 $ in 32 bits, representing the maximum 32-bit unsigned integer.

## 7. Practical Insights

 1. **Digit Tracking:** Be mindful of the digits valid for each base (0/1 for binary, 0-F for hexadecimal).
 2. **Leading Zeros:** Often used to denote fixed-width bit representations (e.g., 32-bit words), without changing the numerical value.
 3. **Hex and Binary Shortcut:** 1 hexadecimal digit corresponds to exactly 4 binary digits, enabling quick conversions between hexadecimal and binary.

## 8. Quick Reference: Common Equations & Meanings

 - **Number in base $b$:**
   $ (d_n d_{n-1} ... d_1 d_0)_b = \sum_{i=0}^{n} \text{value}(d_i) \times b^i $

 - **Decimal to base $b$ conversion:**
   - Repeated division by $b$ and collecting remainders.

 - **Base $b$ to decimal conversion:**
   - Polynomial expansion: $ \sum_{i=0}^{n} \text{value}(d_i) \times b^i $.

**Notation Clarifications:**
 - $ b $ is the base (radix), an integer $ \geq 2 $.
 - $ d_i $ is the digit in position $ i $.
 - $ \text{value}(d_i) $ is the decimal value of the digit symbol (e.g., if $ d_i $ is "A" in base 16, $ \text{value}(d_i) = 10 $).

## How to Use This Guide:

 1. **Identify the Base:** Determine the base of the number you are working with (binary, octal, decimal, hexadecimal).
 2. **Check Symbols:** For bases like hexadecimal, remember the symbol-value mappings (A=10, B=11, etc.).
 3. **Apply Conversion Methods:** Use polynomial expansion or repeated division/multiplication for base conversions.
 4. **Note Base Indicators:** Pay attention to subscripts or prefixes to correctly interpret the base of a number.

By understanding these notations and practicing base conversions, you will enhance your ability to work with numbers in different bases, which is essential in computer systems and low-level programming.

---
*End of Week 1 Notation Guide*
