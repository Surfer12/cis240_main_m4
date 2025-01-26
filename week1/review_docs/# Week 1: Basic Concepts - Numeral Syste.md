# Week 1: Basic Concepts - Numeral Systems

Below is a concise outline and breakdown of the first two pages you’ve shared. It covers the main ideas, definitions, and examples, making it easier to grasp the flow of concepts around numeral systems, their notation, and conversion methods.

## 1. Overview of Positional Numeral Systems

### 1.1. Definition & Purpose
- A positional numeral system represents numbers using digits that each have a place value.
- The base (or radix) determines which digits/symbols are valid and how each digit’s position contributes to the number’s total value.

### 1.2. Annotated Notation
- **Subscripted suffix notation:** e.g., \(11_{10}\) means the number eleven in base 10, \(11_2\) means the number three (binary representation).
- **Programming prefix notation:**
    - `0b` for binary (base 2)
    - `0` for octal (base 8)
    - `0x` for hexadecimal (base 16)
    - No prefix for decimal (base 10)

## 2. Symbol Sets for Various Bases

### 2.1. Common Digits
- **Binary (base 2):** uses digits 0, 1
- **Octal (base 8):** uses digits 0–7
- **Decimal (base 10):** uses digits 0–9
- **Hexadecimal (base 16):** uses digits 0–9 and letters A–F

### 2.2. Value of Extended Symbols in Hexadecimal
- A = 10
- B = 11
- C = 12
- D = 13
- E = 14
- F = 15

### 2.3. Table of Digits & Their Values
- Demonstrates which symbol sets are used by each base and how each symbol maps to its integer value.

## 3. Examples: Representations of Numbers in Multiple Bases

### 3.1. Table for 0–20
- Shows each integer from 0 to 20 in four systems:
    - Hexadecimal (base 16)
    - Decimal (base 10)
    - Octal (base 8)
    - Binary (base 2)
- Highlights that the same “value” is just shown in different symbols depending on the base.
- E.g., decimal 10 is “A” in hexadecimal, “12” in octal, and “1010” in binary.

## 4. Converting Numbers Between Bases

### 4.1. Common Task in Programming & Debugging
- Often humans convert everything to decimal for easier reasoning, then back to another base when necessary (binary, octal, hex) for machine-level detail.

### 4.2. General Formula (Decimal Value Calculation)
$$
d = \sum_{i=0}^{n-1} v_i \times r^i
$$
- Where \(v_i\) is the \(i\)-th digit from the right in base \(r\), and \(d_i\) is that digit’s numerical value.

### 4.3. Reverse Conversion (Decimal to Another Base)
- Uses the idea of repeatedly dividing by the base \(r\), tracking:
    - Quotient (to be divided again)
    - Remainder (the digit in the target base)
- A function like `symbol_from_value(remainder, base)` maps numeric remainders to symbols (e.g., remainder 11 → “B”).

### 4.4. Algorithmic Steps
1. Divide the decimal number \(D\) by base \(r\).
2. The remainder is the symbol for the least-significant digit (\(d_0\)).
3. Set \(D\) to the quotient.
4. Repeat until \(D\) is 0; each remainder becomes the next digit (moving upwards in place value).
5. Reverse the collected digits at the end (or prepend each new digit).

## 5. Key Points & Observations
- **Notation Matters:** In math texts, subscripts often denote bases (\(N_b\)). In many programming languages, prefixes (`0b`, `0x`, `0`) achieve the same clarity.
- **Different Bases, Same Value:** 12 (decimal) = “C” (hex), = “14” (octal), = “1100” (binary).
- **Conversion Process:**
    - From base \(r\) to decimal: multiply each digit by \(r^i\) and sum.
    - From decimal to base \(r\): repeatedly divide by \(r\) and record remainders.

## Tips for Studying or Taking Notes
- **Create Your Own Examples:** Converting a familiar decimal number into binary or hex helps cement the algorithm.
- **Use Shortcut Patterns:**
    - Powers of 2 for binary
    - Group bits in sets of 3 for octal, or 4 for hex.
- **Keep a Reference Table:** Especially for the mappings 0–15 to 0–F when dealing with hexadecimal.

## In Summary
The first two pages give a foundational explanation of positional numeral systems—how we represent numbers in base 2, 8, 10, and 16, and the mechanics of converting among them. They detail both the rationale (why we need different bases in computing) and the step-by-step process (formulas, algorithms) to perform conversions.

This breakdown should help you see the logical sequence: (1) introduction of notation → (2) definitions of symbols per base → (3) examples in tabular form → (4) formal conversion formulas/algorithms.