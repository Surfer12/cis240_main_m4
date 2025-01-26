# Step-by-Step Conversion from Decimal to Binary

This document provides a detailed walkthrough of how to convert a decimal number to its binary representation. We will cover both the integer part and the fractional part of the number.

## 1. Big-Picture Overview

Converting a decimal number to binary involves determining which powers of 2 sum up to the given number.

- **Integer Part**: Found by subtracting the largest powers of 2 that fit into the integer.
- **Fractional Part**: Found by repeatedly multiplying by 2 and checking for a carryover of 1 vs. 0.

## 2. Example: Converting 11.25 to Binary

Let's break down the conversion process step by step for the number 11.25.

### 2.1 Split into Integer and Fractional Parts

- **Integer Part**: 11
- **Fractional Part**: 0.25

### 2.2 Integer Part (11) to Binary

To convert the integer part to binary, we can use the "spreadsheet" approach to see which powers of 2 compose the number 11.

#### Integer Powers of 2 Table

| Power of 2 | Fits into 11? | Remainder |
|------------|----------------|-----------|
| 2^3 (8)    | Yes            | 3         |
| 2^2 (4)    | Yes            | 3         |
| 2^1 (2)    | Yes            | 1         |
| 2^0 (1)    | Yes            | 0         |

So, the binary representation of 11 is 1011.

### 2.3 Fractional Part (0.25) to Binary

To convert the fractional part to binary, we use the following method:

1. Multiply the fractional part by 2.
2. If the result is ≥ 1, the bit is 1; subtract 1 and continue.
3. If the result is < 1, the bit is 0; keep the fractional result and continue.

#### Fractional Part Example

| Step | Fractional Part | Multiplied by 2 | Bit | Remainder |
|------|-----------------|-----------------|-----|-----------|
| 1    | 0.25            | 0.5             | 0   | 0.5       |
| 2    | 0.5             | 1.0             | 1   | 0.0       |

So, the binary representation of 0.25 is 0.01.

### 2.4 Combine Integer and Fractional Parts

The binary representation of 11.25 is 1011.01.

## 3. General Conversion Process

### 3.1 Integer Part Conversion

1. Divide the integer part by 2.
2. Record the remainder (0 or 1).
3. Use the quotient for the next division.
4. Repeat until the quotient is 0.
5. The binary digits are the remainders in reverse order.

### 3.2 Fractional Part Conversion

1. Multiply the fractional part by 2.
2. If the result is ≥ 1, the bit is 1; subtract 1 and continue.
3. If the result is < 1, the bit is 0; keep the fractional result and continue.
4. Repeat until the fractional part is 0 or a maximum number of iterations is reached.

## 4. Visual Recap

### Integer Part Conversion 