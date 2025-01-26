 "Representing Numbers and other in Binary" and "2's Complement".

 Binary 2 and Base 10

1. **Introduction to Microarchitecture**
    - What is microarchitecture?
    - Why is it important for programmers (especially in C)?
    - Abstraction layers in computer systems (hardware, microarchitecture, ISA, OS, application)

2. **Number Representation in Binary**
    - Binary number system basics
    - Bits, bytes, words
    - Representing unsigned integers
    - Representing signed integers
        - Sign-magnitude
        - One's complement
        - **Two's complement** (emphasize this as it's in the original selection and widely used)
    - Hexadecimal representation (for easier reading of binary)

    ### 2.1 Decimal - Base 10
    - Our everyday number system.
    - Uses ten digits (0-9).
    - Each position represents a power of 10.
    - Example: `365 = 3 * 10^2 + 6 * 10^1 + 5 * 10^0`

    ### 2.1.1 Negative Base Number Systems
    - Negative base systems use a negative number as the base.
    - Example: Base -10 (negadecimal)
    - Digits used are the same as in the positive base system (0-9 for base -10).
    - Each position represents a power of the negative base.

    #### 2.1.1.1 Base -10 (Negadecimal)
    - Example: `1234` in base -10
        - `1 * (-10)^3 + 2 * (-10)^2 + 3 * (-10)^1 + 4 * (-10)^0`
        - `-1000 + 200 - 30 + 4 = -826` (in decimal)

    #### 2.1.1.2 Converting to Base -10
    - Similar to converting to a positive base, but with alternating signs.
    - **Repeated Division by -10 Method:**
        1. Divide the decimal number by -10.
        2. Note the remainder (0-9).
        3. Divide the quotient by -10.
        4. Repeat steps 2 and 3 until the quotient is 0.
        5. The negadecimal representation is the sequence of remainders in reverse order.
    - Example: Convert 25 (decimal) to base -10:
        - 25 / -10 = -2, remainder 5
        - -2 / -10 = 1, remainder 8
        - 1 / -10 = 0, remainder 1
        - Base -10: 185

    #### 2.1.1.3 Converting from Base -10
    - **Positional Weight Method:**
        1. Multiply each digit by its corresponding power of -10.
        2. Sum the results.
    - Example: Convert 185 (base -10) to decimal:
        - `1*(-10)^2 + 8*(-10)^1 + 5*(-10)^0 = 100 - 80 + 5 = 25`

    #### 2.1.1.4 Table of Base -10 Values

    | Decimal | Base -10 |
    |---|---|
    | 0 | 0 |
    | 1 | 1 |
    | 2 | 2 |
    | 3 | 3 |
    | 4 | 4 |
    | 5 | 5 |
    | 6 | 6 |
    | 7 | 7 |
    | 8 | 8 |
    | 9 | 9 |
    | 10 | 190 |
    | 11 | 191 |
    | 12 | 192 |
    | -1 | 9 |
    | -2 | 8 |
    | -3 | 7 |
    | -4 | 6 |
    | -5 | 5 |
    | -6 | 4 |
    | -7 | 3 |
    | -8 | 2 |
    | -9 | 1 |
    | -10 | 10 |
    | -11 | 11 |
    | -12 | 12 |
    
    ### 2.2 Binary - Base 2
    - The fundamental number system for computers.
    - Uses two digits (0 and 1), called bits.
    - Each position represents a power of 2.
    - Example: `1011 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 8 + 0 + 2 + 1 = 11` (in decimal)

    ### 2.3 Converting Between Decimal and Binary
    #### 2.3.1 Decimal to Binary
    - **Repeated Division by 2 Method:**
        1. Divide the decimal number by 2.
        2. Note the remainder (0 or 1).
        3. Divide the quotient by 2.
        4. Repeat steps 2 and 3 until the quotient is 0.
        5. The binary representation is the sequence of remainders in reverse order.
    - Example: Convert 25 (decimal) to binary:
        - 25 / 2 = 12, remainder 1
        - 12 / 2 = 6, remainder 0
        - 6 / 2 = 3, remainder 0
        - 3 / 2 = 1, remainder 1
        - 1 / 2 = 0, remainder 1
        - Binary: 11001

    #### 2.3.2 Binary to Decimal
    - **Positional Weight Method:**
        1. Multiply each bit by its corresponding power of 2.
        2. Sum the results.
    - Example: Convert 11001 (binary) to decimal:
        - `1*2^4 + 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 16 + 8 + 0 + 0 + 1 = 25`

    ### 2.4 Representing Unsigned Integers
    - All bits represent the magnitude of the number.
    - Range for n bits: 0 to 2^n - 1
    - Example: 8-bit unsigned integer range: 0 to 255 (0 to 2^8 - 1)

    ### 2.5 Representing Signed Integers
    #### 2.5.1 Sign-Magnitude
    - The most significant bit (MSB) represents the sign (0 for positive, 1 for negative).
    - Remaining bits represent the magnitude.
    - Example: In 8-bit sign-magnitude, +5 is 00000101, -5 is 10000101.
    - Drawback: Two representations for zero (+0 and -0).

    #### 2.5.2 One's Complement
    - Positive numbers are represented as in unsigned binary.
    - Negative numbers are represented by inverting all bits of the corresponding positive number.
    - Example: In 8-bit one's complement, +5 is 00000101, -5 is 11111010.
    - Drawback: Still two representations for zero.

    #### 2.5.3 Two's Complement
    - Most common representation for signed integers.
    - Positive numbers are represented as in unsigned binary.
    - **Negative numbers are represented by inverting all bits of the corresponding positive number and adding 1.** This process is also known as taking the two's complement of the positive number.
    - Example: In 8-bit two's complement, +5 is 00000101, -5 is 11111011.
        - To find the representation of -5:
            1. Start with the binary representation of +5: 00000101
            2. Invert all the bits: 11111010
            3. Add 1 to the result: 11111010 + 1 = 11111011
    - **Identifying a negative number:**
        - **A number is negative in two's complement if its most significant bit (MSB) is 1.**
        - To find the magnitude of a negative number:
            1. Invert all the bits.
            2. Add 1 to the result.
            3. Interpret the result as an unsigned binary number. This gives the magnitude of the negative number.
        - Example: Given the 8-bit two's complement number 11111011:
            1. The MSB is 1, so it's a negative number.
            2. Invert all the bits: 00000100
            3. Add 1: 00000100 + 1 = 00000101
            4. Interpret as unsigned binary: 00000101 = 5
            5. Therefore, 11111011 represents -5.
    - **Advantages:**
        - Single representation for zero.
        - Addition and subtraction can be performed using the same hardware as for unsigned integers.
    - Range for n bits: -2^(n-1) to 2^(n-1) - 1
    - Example: 8-bit two's complement range: -128 to 127 (-2^7 to 2^7 - 1)

    ### 2.6 Hexadecimal Representation
    - Base 16 number system.
    - Uses digits 0-9 and letters A-F (A=10, B=11, ..., F=15).
    - Each hexadecimal digit represents 4 bits.
    - Convenient for representing binary numbers in a more compact form.
    - Example: Binary 11110110 is F6 in hexadecimal (1111 = F, 0110 = 6).
    - Conversion between binary and hexadecimal is straightforward.

3. **Representing Other Data in Binary**
    - Characters (ASCII, Unicode)
    - Floating-point numbers (brief overview, IEEE 754)
    - Instructions (briefly touch upon instruction encoding)
    - Memory addresses

4. **C Data Types and their Binary Representation**
    - `int`, `char`, `float`, `double`, etc.
    - Size and range of data types
    - Memory layout of variables

5. **Bitwise Operations in C**
    - AND, OR, XOR, NOT, left shift, right shift
    - Applications of bitwise operations (e.g., masking, setting/clearing bits)
    - C code examples demonstrating bitwise operations

6. **Microarchitectural Concepts (brief introduction, can be expanded in later lectures)**
    - Registers
    - Arithmetic Logic Unit (ALU)
    - Control Unit
    - Memory hierarchy (cache, main memory)
    - Instruction Fetch-Decode-Execute cycle

7. **Conclusion**
    - Recap of key concepts
    - Importance of understanding binary representation and microarchitecture for efficient C programming

I will format this as a markdown outline, suitable for a lecture note in `lecture_1/lecture_1.md`. I will use headings and bullet points for clarity. I will also add a brief introduction and conclusion to frame the lecture.```
// Start of Selection
# Lecture 1: Introduction to Microarchitecture and Binary Representation in C

## 1. Introduction to Microarchitecture

### 1.1 What is Microarchitecture?
- The underlying implementation of the Instruction Set Architecture (ISA).
- Deals with how the CPU is internally organized to execute instructions.
- Includes components like:
    - Arithmetic Logic Unit (ALU)
    - Registers
    - Control Unit
    - Cache and Memory Hierarchy
    - Interconnects and Buses

### 1.2 Why Microarchitecture Matters for C Programmers
- Understanding performance implications of C code at a lower level.
- Optimizing code for specific architectures (though often compilers handle this).
- Debugging and understanding hardware-related issues.
- Writing efficient low-level code (e.g., embedded systems, device drivers).
- Gaining a deeper appreciation for how software interacts with hardware.

### 1.3 Abstraction Layers in Computing
- **Hardware Level:** Physical components (transistors, gates, circuits).
- **Microarchitecture Level:** Organization of CPU components to execute instructions.
- **Instruction Set Architecture (ISA) Level:**  The programmer's view of the machine (instructions, registers, memory model).
- **Operating System Level:** Manages hardware resources and provides services to applications.
- **Application Level:** Software programs written by users.
- **C as a Bridge:** C language provides relatively low-level access and control, making microarchitecture understanding relevant.

## 2. Representing Numbers in Binary

### 2.1 Binary Number System Basics
- Base-2 number system using only 0 and 1.
- Each digit is a **bit** (binary digit).
- Positional notation: each position represents a power of 2.
    - Example: `1011_2 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 8 + 0 + 2 + 1 = 11_{10}`

### 2.2 Bits, Bytes, Words
- **Bit:** The fundamental unit of information (0 or 1).
- **Byte:**  A group of 8 bits (historically, the smallest addressable unit of memory).
- **Word:**  A natural unit of data for a particular architecture (e.g., 32-bit word, 64-bit word). Word size affects register size and memory addressing.

### 2.3 Representing Unsigned Integers
- Direct binary representation.
- Range for *n* bits: 0 to 2<sup>n</sup> - 1.
- Example (8-bit unsigned integer): 00000000 (0) to 11111111 (255).

### 2.4 Representing Signed Integers
- Challenges: Need to represent both positive and negative numbers.
- Common methods:
    - **Sign-Magnitude:**
        - One bit for sign (0 for positive, 1 for negative).
        - Remaining bits for magnitude.
        - Problem: Two representations for zero (+0 and -0), complex arithmetic.
    - **One's Complement:**
        - Positive numbers: same as unsigned binary.
        - Negative numbers: Invert all bits of the positive representation.
        - Problem: Still two representations for zero, complex arithmetic.
    - **Two's Complement:**
        - Positive numbers: same as unsigned binary.
        - Negative numbers: Invert all bits of the positive representation and add 1.
        - **Advantages of Two's Complement:**
            - Only one representation for zero.
            - Simpler arithmetic, especially addition and subtraction.
            - Widely used in modern computers.

### 2.5 Two's Complement in Detail

#### 2.5.1 Conversion to Two's Complement (for negative numbers)
1. Start with the positive binary representation.
2. Invert all the bits (0s become 1s, 1s become 0s) - **One's Complement**.
3. Add 1 to the result - **Two's Complement**.

    *Example: Represent -5 in 8-bit two's complement.*
    1. +5 in binary: `00000101`
    2. Invert bits (One's Complement): `11111010`
    3. Add 1: `11111011`  (-5 in two's complement)

#### 2.5.2 Range of Two's Complement (for *n* bits)
- From -2<sup>(n-1)</sup> to 2<sup>(n-1)</sup> - 1.
- Example (8-bit two's complement): -128 to +127.

#### 2.5.3 Sign Extension in Two's Complement
- When converting a two's complement number with *n* bits to *m* bits (*m* > *n*), preserve the sign by extending the most significant bit (sign bit) to the left.
- Example: 4-bit `-3` (`1101`) to 8-bit: `11111101`.

### 2.6 Hexadecimal Representation
- Base-16 number system (digits 0-9, A-F).
- Used as a shorthand for binary, as each hexadecimal digit represents 4 bits.
- Easier for humans to read and write long binary numbers.
- Conversion between binary and hexadecimal is straightforward.

    *Example: Binary `10111010 00011110` in hexadecimal.*
    - Group bits in 4s: `1011 1010 0001 1110`
    - Convert each group to hex: `B  A   1   E`
    - Hexadecimal: `BA1E`

## 3. Representing Other Data in Binary (Brief Overview)

### 3.1 Characters (ASCII, Unicode)
- Characters are represented by numerical codes.
- **ASCII:** 7-bit encoding for English characters (extended ASCII uses 8 bits).
- **Unicode:**  A more comprehensive standard to represent characters from almost all writing systems in the world (uses variable number of bytes, often UTF-8).

### 3.2 Floating-Point Numbers (IEEE 754)
- Representing real numbers with fractional parts.
- **IEEE 754 Standard:**  Defines formats for single-precision (32-bit) and double-precision (64-bit) floating-point numbers.
- Components: Sign bit, exponent, mantissa (fraction).

### 3.3 Instructions
- Machine instructions are also encoded in binary.
- Instruction format varies depending on the ISA.
- Includes opcode (operation to perform) and operands (data or addresses).

### 3.4 Memory Addresses
- Memory locations are identified by numerical addresses, represented in binary.
- Address size determines the addressable memory space (e.g., 32-bit addresses for 4GB address space, 64-bit for much larger).

## 4. C Data Types and Binary Representation

### 4.1 Basic C Data Types
- `char`: Typically 1 byte (8 bits). Represents characters (ASCII or extended ASCII).
- `short`: Typically 2 bytes (16 bits). Short integer.
- `int`:  Typically 4 bytes (32 bits) or 8 bytes (64 bits) depending on the architecture. Integer.
- `long`: Typically 8 bytes (64 bits). Long integer.
- `float`: Typically 4 bytes (32 bits). Single-precision floating-point.
- `double`: Typically 8 bytes (64 bits). Double-precision floating-point.

### 4.2 Size and Range in C
- `sizeof()` operator in C to determine the size of data types on a specific system.
- `<limits.h>` and `<float.h>` header files provide macros defining the ranges and limits of data types.

### 4.3 Memory Layout of Variables
- Variables in C are stored in memory as sequences of bytes.
- Data type determines how many bytes are allocated and how they are interpreted.
- Endianness (byte order) can affect how multi-byte data is stored in memory (little-endian vs. big-endian).

## 5. Bitwise Operations in C

### 5.1 Bitwise Operators
- `&` (Bitwise AND)
- `|` (Bitwise OR)
- `^` (Bitwise XOR)
- `~` (Bitwise NOT - One's Complement)
- `<<` (Left Shift)
- `>>` (Right Shift)

### 5.2 Applications of Bitwise Operations
- **Masking:** Extracting specific bits from a value using AND.
- **Setting Bits:**  Setting specific bits to 1 using OR.
- **Clearing Bits:** Setting specific bits to 0 using AND with a mask and NOT.
- **Toggling Bits:** Inverting specific bits using XOR.
- **Bit Shifting:** Efficiently multiplying or dividing by powers of 2.

### 5.3 C Code Examples (Illustrative)
A wire in a computer system serves as the fundamental conduit for transmitting information. This information is encoded in binary form, using two distinct voltage levels. Traditionally, these levels have been 0 volts (0v) and 5 volts (5v). However, advancements in technology have led to the adoption of lower voltages in modern systems to enhance energy efficiency and reduce heat generation. For instance, some systems might use 3.3v, 1.8v, or even lower voltages to represent the 'high' state.

The interpretation of these voltage levels as logical states is crucial for digital computation. Let's break down the common interpretation:

*   **0 volts (0v):** This level is universally interpreted as **LOGIC 0**, representing the logical state **FALSE**. In conceptual terms, this can be visualized as the system being in an "off" or "low" state.
*   **5 volts (5v) or lower (e.g., 3.3v, 1.8v):** This level is interpreted as **LOGIC 1**, representing the logical state **TRUE**. Conceptually, this corresponds to the system being in an "on" or "high" state.

It's paramount to understand that the precise voltage levels and their corresponding logical interpretations are not arbitrary. They are meticulously defined by the computer's designer, taking into account the specific logic family employed in the system's circuitry. Different logic families, such as Transistor-Transistor Logic (TTL) and Complementary Metal-Oxide-Semiconductor (CMOS), have their own unique voltage thresholds and characteristics.

I should expand on these points, clarify the phrasing, and provide more context for a lecture setting.

Here's a possible expansion plan:
- Clarify the voltage levels and their relation to logic levels.
- Explain the "off, on, low, high" terminology and standardize it.
- Briefly mention different logic families (though maybe too detailed for an intro lecture).
- Emphasize the bit as the fundamental unit of information.
- Explain the abstraction from physical voltage to logical 0 and 1.
- Connect this to the concept of binary representation discussed in the surrounding lecture notes

For example, in classic TTL, a voltage between 0v and 0.8v might be considered LOGIC 0, while a voltage between 2v and 5v might be considered LOGIC 1. In CMOS, the thresholds might be different, and the voltage representing LOGIC 1 could be significantly lower than 5v.

Despite these variations, the underlying principle remains steadfast: two distinct voltage ranges are employed to represent the binary digits 0 and 1.

Each individual wire or memory cell within the computer's intricate architecture that can maintain one of these two distinct voltage states is referred to as a **bit**. The bit stands as the fundamental, indivisible unit of information in digital systems. It embodies a binary digit, which can exist in one of two possible states: 0 or 1.

Thus, the seemingly elementary concept of a wire carrying either 0v or a higher voltage (like 5v, 3.3v, or 1.8v) forms the very bedrock upon which all digital information is represented within a computer. These voltage states, interpreted as sequences of LOGIC 0s and LOGIC 1s, are the foundation of data storage, processing, and communication in the digital realm.

A bit (binary digit) is one of the two values that can be stored in a computer. The physical representation of a bit can vary, but it fundamentally represents a choice between two states. These states can be represented by different voltage levels on a wire, the presence or absence of an electrical charge in a memory cell, the direction of magnetization on a magnetic disk, or the reflection or absorption of light on an optical disc.


