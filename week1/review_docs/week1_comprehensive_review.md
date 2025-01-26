# Week 1 Comprehensive Review: Foundations of Computer Systems

This document synthesizes key concepts from Week 1 of CIS 240, drawing from various review materials to provide a comprehensive overview. We will cover binary arithmetic, numeral systems, base conversions, and an outline of the course map, linking these fundamental ideas to the broader landscape of computer systems.

## 1. Binary Arithmetic and Number Representation

### 1.1. Binary Arithmetic: Addition and Subtraction

Computers operate using binary digits (bits), so understanding binary arithmetic is crucial.

**Binary Addition:**

Binary addition is similar to decimal addition but with only two digits: 0 and 1.  When adding two bits:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (0 with a carry of 1)

Carry bits propagate to the next more significant position, just like in decimal addition.

**Binary Subtraction:**

Binary subtraction also mirrors decimal subtraction, but borrowing occurs when subtracting a larger bit from a smaller one.
- 0 - 0 = 0
- 1 - 0 = 1
- 1 - 1 = 0
- 0 - 1 = Borrow 1 from the next more significant bit, resulting in 10 - 1 = 1

Borrow bits propagate from more significant positions when needed.

**Example (3-bit Addition and Subtraction):**

Refer to Figures 2.4 and 2.5 in your readings for visual diagrams of binary addition and subtraction circuits. These diagrams illustrate how carry and borrow bits are managed at the digital logic level.

### 1.2. Overflow

Overflow occurs when the result of an arithmetic operation exceeds the maximum value that can be represented with the available number of bits.

**Example:** In a 3-bit system, the largest unsigned number is 111 (binary) = 7 (decimal).  If you add 7 + 1:- 111 (7)
+ 001 (1)
-----
1000 (8)

The result, 8, requires 4 bits to represent. In a 3-bit system, overflow occurs, and the result might wrap around or be misinterpreted, depending on the system's handling of overflow.

### 1.3. Signed vs. Unsigned Numbers

- **Unsigned Numbers:** Represent only non-negative values (zero and positive numbers). With *n* bits, you can represent numbers from 0 to 2<sup>*n*</sup> - 1.
- **Signed Numbers:** Represent both positive and negative values. Several methods exist for representing signed numbers:

    - **Sign and Magnitude:** The leftmost bit represents the sign (0 for positive, 1 for negative), and the remaining bits represent the magnitude.
    - **One's Complement:** Negative numbers are obtained by inverting all bits of the positive representation.
    - **Two's Complement:** Negative numbers are obtained by inverting all bits of the positive representation and adding 1. Two's complement is the most widely used representation for signed integers in modern computers because it simplifies arithmetic operations and has a unique representation for zero.

**Two's Complement in Detail:**

Two's complement is favored because addition and subtraction work seamlessly for both positive and negative numbers using the same hardware circuits.  For an *n*-bit two's complement representation, the range is from -2<sup>*n*-1</sup> to 2<sup>*n*-1</sup> - 1.

**Practical Check:**

Take a few 3-bit or 4-bit numbers and perform binary addition and subtraction manually.  Experiment with signed and unsigned representations to understand overflow and the behavior of two's complement.

## 2. Positional Numeral Systems and Base Conversions

### 2.1. Positional Numeral Systems

A positional numeral system represents numbers using digits where each digit's value depends on its position and the base (radix) of the system. The base defines the number of unique digits available in the system.

**Common Bases in Computing:**

- **Binary (Base 2):** Digits: 0, 1. Prefix: `0b` (e.g., `0b1010`).
- **Octal (Base 8):** Digits: 0-7. Prefix: `0` (e.g., `012`).
- **Decimal (Base 10):** Digits: 0-9. No prefix.
- **Hexadecimal (Base 16):** Digits: 0-9, A-F (A=10, B=11, C=12, D=13, E=14, F=15). Prefix: `0x` (e.g., `0xA`).

**Notation:**

- Subscript notation: 11<sub>10</sub> (decimal eleven), 3<sub>2</sub> (binary three).
- Programming prefixes: `0b`, `0`, `0x` for binary, octal, and hexadecimal respectively.

### 2.2. Converting Between Bases

Converting between bases is a common task in programming and computer architecture.

**Decimal to Binary Conversion:**

**Integer Part:**
1. **Repeated Division:** Divide the decimal integer by 2.
2. **Record Remainder:** The remainder (0 or 1) is the least significant bit (LSB).
3. **Update Quotient:**  Set the quotient as the new number to divide.
4. **Repeat:** Continue steps 1-3 until the quotient becomes 0.
5. **Reverse Remainders:** The binary representation is the sequence of remainders in reverse order of their calculation.

**Fractional Part:**
1. **Repeated Multiplication:** Multiply the decimal fraction by 2.
2. **Record Integer Part:** If the result is ≥ 1, the binary bit is 1; otherwise, it's 0.
3. **Update Fraction:** If the bit was 1, subtract 1 from the result to get the new fractional part. Otherwise, use the result as is.
4. **Repeat:** Continue steps 1-3 until the fractional part becomes 0 or you reach the desired precision.
5. **Sequence Bits:** The binary representation is the sequence of integer parts obtained in order.

**Example: Convert 11.25 (decimal) to binary:**

**Integer Part (11):**
| Division | Quotient | Remainder | Binary Digit (Reverse Order) |
|---|---|---|---|
| 11 ÷ 2 | 5 | 1 | 1 |
| 5 ÷ 2 | 2 | 1 | 1 |
| 2 ÷ 2 | 1 | 0 | 0 |
| 1 ÷ 2 | 0 | 1 | 1 |
Binary Integer Part: `1011`

**Fractional Part (0.25):**
| Multiplication | Result | Integer Part | Binary Digit | Fractional Part (Next Iteration) |
|---|---|---|---|---|
| 0.25 × 2 | 0.5 | 0 | 0 | 0.5 |
| 0.5 × 2 | 1.0 | 1 | 1 | 0.0 |
Binary Fractional Part: `.01`

**Combined Binary Representation: `1011.01`**

**General Formula for Decimal Value Calculation from any Base:**

For a number in base *b*:  d<sub>n</sub>d<sub>n-1</sub>...d<sub>1</sub>d<sub>0</sub>.d<sub>-1</sub>d<sub>-2</sub>...d<sub>-m</sub>

Decimal Value =  ∑<sup>n</sup><sub>i=-m</sub> d<sub>i</sub> * b<sup>i</sup>

**Tips for Practice:**

- Convert familiar decimal numbers (like powers of 10, or small integers) to binary, octal, and hexadecimal.
- Use online base converters to check your manual conversions.
- Practice converting in both directions (decimal to other bases and vice versa).

## 3. Course Map Overview and Key Concepts

The course map provides a high-level view of how different components and concepts in computer systems are interconnected.

**Major Themes in the Course Map:**

1. **Signals (Data/Numbers):**  Understanding how data is represented as binary signals and transmitted within a computer.
2. **Digital Circuits (Gates, Boolean Logic):**  Exploring the fundamental building blocks of digital systems – logic gates – and how they implement Boolean logic. This includes truth tables and Karnaugh maps for circuit simplification.
3. **Compilers (Toolchain):**  Tracing the stages of compilation from high-level source code to executable machine code (Preprocessor → Compiler → Assembler → Linker).
4. **Languages / Instruction Hardware (Assembly, Machine Language, Architecture):**  Learning about low-level programming languages (Assembly), the binary instructions that CPUs execute (Machine Language), and the underlying hardware architecture (e.g., RISC-V, x86).
5. **Memory (Addressing Schemes):**  Studying how memory is organized, addressed, and accessed by the CPU, including different addressing modes (direct, indirect, etc.).
6. **Memory-Mapped I/O:**  Understanding how specific memory addresses are used to interact with peripheral devices, enabling software control of hardware.
7. **Motherboard Components:**  Identifying key components on a motherboard (CPU, Northbridge, Southbridge, memory slots, I/O interfaces) and their roles in the system.

**Course Map - Conceptual Flow:**

- **Digital Logic** (gates, Boolean algebra) forms the foundation for building **Digital Circuits**.
- **Digital Circuits** implement the operations needed by the **CPU Architecture**.
- **CPU Architecture** executes **Machine Language** instructions.
- **Assembly Language** provides a human-readable representation of **Machine Language**.
- **Compilers** translate high-level languages into **Assembly Language** and ultimately **Machine Language**.
- **Memory** stores both data and instructions in binary form.
- **Memory-Mapped I/O** allows the CPU to communicate with **I/O Devices** by accessing specific memory addresses.
- All these components are physically connected and managed by the **Motherboard**.

**Suggested Learning Path (Based on Course Map):**

1. **Digital Logic:** Start with logic gates, Boolean algebra, and circuit simplification.
2. **Computer Architecture Basics:** Understand CPU structure, memory hierarchy, and bus interfaces.
3. **Assembly & Machine Language:** Learn basic assembly programming and the relationship to machine code.
4. **Compiler Toolchain:** Explore the stages of compilation and how source code becomes executable.
5. **Memory-Mapped I/O:** Investigate how software interacts with hardware through memory addresses.

## 4. Homework Walkthrough: Decimal to Binary Conversion Example (11.25)

As demonstrated earlier, converting 11.25 from decimal to binary involves separate processes for the integer and fractional parts. The "spreadsheet" or tabular approach helps visualize the steps:

**Integer Part (11):**

| Power (2<sup>n</sup>) | Value | Does 11 fit? | Binary Bit | Remaining Value |
|---|---|---|---|---|
| 2<sup>3</sup> | 8 | Yes | 1 | 11 - 8 = 3 |
| 2<sup>2</sup> | 4 | No (4 > 3) | 0 | 3 |
| 2<sup>1</sup> | 2 | Yes | 1 | 3 - 2 = 1 |
| 2<sup>0</sup> | 1 | Yes | 1 | 1 - 1 = 0 |
Binary Integer Part: `1011`

**Fractional Part (0.25):**

| Power (2<sup>-n</sup>) | Value | Is fraction ≥ value? | Binary Bit | New Fraction |
|---|---|---|---|---|
| 2<sup>-1</sup> | 0.5 | No (0.25 < 0.5) | 0 | 0.25 |
| 2<sup>-2</sup> | 0.25 | Yes | 1 | 0.25 - 0.25 = 0.0 |
Binary Fractional Part: `.01`

**Combined Binary: `1011.01`**

This systematic approach ensures accuracy and helps in understanding the underlying principles of base conversion.

## Conclusion

This comprehensive review covers the foundational concepts of Week 1, including binary arithmetic, number representations, base conversions, and an overview of the course map. Mastering these fundamentals is essential for understanding how computer systems operate at a low level and for progressing through the more advanced topics in the course. Keep practicing base conversions and binary arithmetic, and continually refer back to the course map to see how each concept fits into the larger picture of computer systems.

---
*End of Week 1 Comprehensive Review Document* 
