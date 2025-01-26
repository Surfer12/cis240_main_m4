
**Base-10 to Binary Conversion**

1.  Identify the largest power of 2 that is less than or equal to the base-10 number. [cite: 94]
   
2.  Subtract this power of 2 from the base-10 number. [cite: 94]
   
3.  Place a ‘1’ in the place value corresponding to this power of 2. [cite: 94]
   
4.  Repeat steps 1-3 with the remaining value until the value is 0. [cite: 94]
   
5.  For decimal values, repeat this process with negative powers of 2. [cite: 95]

**Binary to Base-10 Conversion**

1.  Starting with the leftmost bit (or the rightmost bit for decimals), multiply the bit value (1 or 0) by the corresponding power of 2. [cite: 98]
   
2.  Repeat for each bit value. [cite: 98]
   
3.  Add the products together. [cite: 98]

**Binary to Hexadecimal Conversion**

1.  Group bits into 4-bit chunks, starting from the decimal point and moving outwards. [cite: 100]
   
2.  For each 4-bit chunk, calculate its base-10 value. [cite: 100]
   
3.  If the base-10 value is greater than 9, use the corresponding letter (A=10, B=11, C=12, D=13, E=14, F=15). [cite: 100]

**Representing Negative Numbers**

*   **Sign-Magnitude:** Topmost bit (MSB) is the sign bit (1 = negative, 0 = positive). [cite: 103]
   
*   **1’s Complement:** The negative value is the “complement” of the positive value (all 1s changed to 0 and all 0s changed to 1). [cite: 103]
   
*   **2’s Complement:** The negative value is the “complement plus 1” (all 1s changed to 0 and all 0s changed to 1, then add 1). [cite: 103]