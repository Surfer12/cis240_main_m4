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

Conversion Table for 11.25
==============================
Decimal: 11.25
Binary: 1011.01
------------------------------
Integer Part Conversion
Step | Quotient | Remainder
------------------------------
1 | 5 | 1
2 | 2 | 1
3 | 1 | 0
4 | 0 | 1

Fractional Part Conversion
Step | Fractional Part | Multiplied by 2 | Bit | Remainder
------------------------------------------------------------
1 | 0.5 | 0.5 | 0 | 0.5
2 | 1.0 | 2.0 | 1 | 0.0
### Integer Part Conversion 

M
├─ remainder(LSB) = 0 or 1
└─ M // 2 --> new M
Repeat until M = 0
Collect remainders in reverse order => binary


### Fractional Part Conversion
F
├─ Multiply by 2 => x
| └─ if x >= 1 => bit = 1, leftover x-1
| else => bit = 0, leftover x
└─ leftover becomes new F
Repeat until leftover = 0 or you have enough bits

## 5. Conclusion

By following these steps, you can convert any decimal number to its binary representation. This method ensures that both the integer and fractional parts are accurately converted, providing a complete binary representation of the original decimal number.

Explanation
Big-Picture Overview: Explains the general approach to converting decimal numbers to binary.
Example Conversion: Demonstrates the conversion process for the number 11.25, including both the integer and fractional parts.
General Conversion Process: Outlines the step-by-step methods for converting the integer and fractional parts.
Visual Recap: Provides ASCII diagrams to summarize the conversion processes for both integer and fractional parts.
5. Conclusion: Summarizes the key points and emphasizes the accuracy of the conversion method.
This file will help users understand the conversion process step by step, making it easier to follow and apply the method to other decimal numbers.

### Summary of Key Points and Accuracy of Conversion Methods

The conversion methods for decimal to binary and binary to decimal, as implemented in the provided Python files, are designed to handle both integer and fractional parts of decimal numbers accurately. Here are the key points and emphasis on the accuracy of these methods:

#### Decimal to Binary Conversion

**Key Points:**
1. **Input Validation**: The function ensures that the input is either an integer or a float, raising a `ValueError` if the input is invalid.
2. **Integer Part Handling**: The integer part of the decimal number is converted to binary using Python's built-in `bin()` function.
3. **Fractional Part Handling**: The fractional part is handled by repeatedly multiplying by 2 and taking the integer part of the result. This process continues until the fractional part becomes zero or a predefined limit is reached.
4. **Negative Numbers**: The function correctly handles negative decimal numbers by converting the absolute value and then prepending a negative sign to the binary representation.

**Accuracy:**
- The method accurately converts decimal numbers to binary, including both integer and fractional parts.
- The use of a loop with a limit (e.g., 32 iterations) ensures that the function does not enter an infinite loop for non-terminating decimals.
- Test cases demonstrate the function's ability to handle various types of decimal numbers, including positive integers, positive floats, and negative floats.

#### Binary to Decimal Conversion

**Key Points:**
1. **Input Validation**: The function ensures that the input is a string, raising a `ValueError` if the input is invalid.
2. **Integer and Fractional Part Splitting**: The binary number is split into integer and fractional parts using the `.` character as a delimiter.
3. **Integer Part Conversion**: The integer part is converted to decimal using Python's built-in `int()` function with base 2.
4. **Fractional Part Conversion**: The fractional part is converted by summing the contributions of each bit, weighted by powers of 2.
5. **Negative Numbers**: The function correctly handles negative binary numbers by converting the absolute value and then applying the negative sign to the decimal representation.

**Accuracy:**
- The method accurately converts binary numbers to decimal, including both integer and fractional parts.
- The use of enumeration and power of 2 calculations ensures precise conversion of the fractional part.
- Test cases demonstrate the function's ability to handle various types of binary numbers, including positive integers, positive floats, and negative floats.

#### Step-by-Step Table Creation

**Key Points:**
1. **Input Validation**: The function ensures that the input is either an integer or a float, raising a `ValueError` if the input is invalid.
2. **Integer Part Handling**: The integer part of the decimal number is converted to binary, and a step-by-step table is created to show the division process.
3. **Fractional Part Handling**: The fractional part is handled by repeatedly multiplying by 2 and taking the integer part of the result. A step-by-step table is created to show this process.
4. **Table Generation**: The function generates a table that summarizes the conversion process for both the integer and fractional parts.

**Accuracy:**
- The method accurately creates a step-by-step table that shows the conversion process for both the integer and fractional parts of the decimal number.
- The use of loops with limits ensures that the function does not enter an infinite loop for non-terminating decimals.
- Test cases demonstrate the function's ability to handle various types of decimal numbers, including positive integers and positive floats.

### Conclusion

The conversion methods for decimal to binary and binary to decimal, as implemented in the provided Python files, are accurate and robust. They handle both integer and fractional parts of decimal numbers and include input validation to ensure correct usage. The step-by-step table creation method provides a clear and detailed summary of the conversion process, enhancing understanding and verification of the accuracy of the conversions. These implementations are essential for understanding and implementing binary and decimal number conversions in various programming contexts.
