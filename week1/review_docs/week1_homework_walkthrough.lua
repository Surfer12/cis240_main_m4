Below is a step‐by‐step walkthrough of how to convert from decimal (base 10) to binary (base 2), along with some “visual” aids using tables, charts, and spreadsheet‐style layouts. We’ll tackle both the integer part and the fractional (decimal) part of a number.

1. Big‐Picture Overview

Converting a decimal number ￼ to binary essentially answers the question:
@Essential_Question_During_Analysis
	“Which powers of 2 sum up to ￼?”

	•	Integer part (left of the decimal point) is found by subtracting off (or dividing by 2 repeatedly) the largest powers of 2 that “fit” into the integer.
	•	Fractional part (right of the decimal point) is found by repeatedly multiplying by 2 and checking for a carryover of 1 vs. 0.

2. Example #1 (Simpler Demonstration): 11.25 in Base 10

Let’s illustrate with a smaller example—11.25.
	1.	Split into Integer & Fractional Parts
	•	Integer Part: ￼
	•	Fractional Part: ￼
	2.	Integer Part (11) ⇒ Binary
A quick “spreadsheet” approach is to see which powers of 2 compose the number 11.
Integer Powers of 2 Table



So we get the bits from 2^3 down to 2^0 as: 1011.
	Integer Part in Binary = 1011 (which is 8 + 0 + 2 + 1 = 11).

	3.	Fractional Part (0.25) ⇒ Binary
For fractions, the standard method is:
	•	Multiply the fractional part by 2.
	•	If the result ≥ 1, that bit is a 1; subtract 1 and continue.
	•	If the result < 1, that bit is 0; keep the fractional result and continue.
Fractional Part Example

￼
￼
So the first fractional bit is 0, the second is 1.
Hence the fractional part in binary is: .01.
	4.	Combine Integer + Fractional = 11.25
	•	Integer part: 1011
	•	Fractional part: .01
	•	Full binary:
￼

That’s the basic process.

3. Using a “Diagram” or “Flow” Perspective

Below is a flow‐style chart (in text) for the fractional conversion steps. Imagine it as boxes with arrows:

Start with fractional part = 0.25

[Multiply by 2 --> 0.5]
   | result < 1 => bit = 0
   v
[Multiply by 2 --> 1.0]
   | result >= 1 => bit = 1
     Subtract 1 => fractional remainder = 0.0
   v
Stop (fraction = 0.0 => done)

Fractional bits from top to bottom = 0, then 1 => .01

4. Larger Example: Integer Part up to 2^10

Suppose we want to decode something like your mention of 11.25 but ensuring we list out bits for exponents ￼ down to ￼. In practice, we only “light up” the powers of 2 that fit:

Spreadsheet for Integer Part (through 2^10 down to 2^0)


| Power (2^n) | Value | Does 11 fit? | Binary Bit |
|---|---|---|---|
| 2^10 | 1024 | No (1024 > 11) | 0 |
| 2^9  | 512  | No             | 0          |
| 2^8  | 256  | No             | 0          |
| 2^7  | 128  | No             | 0          |
| 2^6  | 64   | No             | 0          |
| 2^5  | 32   | No (32 > 11)   | 0          |
| 2^4  | 16   | No (16 > 11)   | 0          |
| 2^3  | 8    | Yes            | 1          |
| 2^2  | 4    | No (remaining=3) | 0          |
| 2^1  | 2    | Yes (2 ≤ 3)    | 1          |
| 2^0  | 1    | Yes (1 ≤ 1)    | 1          |

So from 2^10 down to 2^0, the bits are:

0 0 0 0 0 0 0 1 0 1 1

which collapses to just 1011 once we drop leading zeros.

5. Fractional Bits for Negative Powers of 2

When you see references to exponents like ￼, these correspond to:
	•	￼
	•	￼
	•	￼
	•	￼
	•	and so forth…

In binary, the first fraction bit after the binary “decimal” point represents ￼, the second bit represents ￼, etc.

Using the same table logic for fractional parts, but now each row is a negative exponent:

Power	Value	Is fraction ≥ that value?	Binary Bit	New fraction
2^-1	0.5	0.25 ≥ 0.5? No	0	0.25
2^-2	0.25	0.25 ≥ 0.25? Yes	1	0.25 − 0.25 = 0.00
2^-3	0.125	fraction = 0.00 => no	0	(already zero)
2^-4	0.0625	fraction = 0.00 => no	0	…
2^-5	0.03125	fraction = 0.00 => no	0	…

Hence for 0.25, the bits out to 5 fractional places would be 0 1 0 0 0, confirming .01 in the first two spots and zeros beyond that.

6. Combined “Master Chart” Approach

Let’s illustrate a master chart that can handle both the integer and fractional bits together. For demonstration, assume we want up to 5 places after the decimal:

Number: ￼

Exponent	Power of 2	Portion	Does it fit?	Bit
2^3	8	Integer portion	8 ≤ 11 ⇒ Yes	1
2^2	4	Integer portion	4 ≤ (11−8)=3 ⇒No	0
2^1	2	Integer portion	2 ≤ 3 ⇒ Yes	1
2^0	1	Integer portion	1 ≤ (3−2)=1 ⇒Yes	1
— decimal —	—	—	—	.
2^-1	0.5	Fraction portion	0.25 ≥ 0.5? ⇒No	0
2^-2	0.25	Fraction portion	0.25 ≥ 0.25⇒Yes	1
2^-3	0.125	Fraction portion	0 leftover ⇒No	0
2^-4	0.0625	Fraction portion	0 leftover ⇒No	0
2^-5	0.03125	Fraction portion	0 leftover ⇒No	0

Hence the bits in order: (1011).(01) and you can pad extra zeros if you want more fractional places.

7. Putting It All Together for a Larger Decimal

If you wanted to do something like ￼, you would:
	1.	Integer part = 652. Subtract off powers of 2 (or repeatedly divide by 2).
	2.	Fractional part = 0.625. Multiply by 2 repeatedly to find bits.

Short breakdown (just to illustrate the pattern for integer “652”):
	•	￼ remainder 0 → LSB is 0
	•	￼ remainder 0 → next bit is 0
	•	￼ remainder 1 → next bit is 1
	•	￼ remainder 1 → next bit is 1
	•	… (continue until the quotient is 0)
	•	Reverse the remainders to get the integer’s binary bits.

For fractional “0.625”:
	•	￼ → bit = 1, leftover fraction = 0.25
	•	￼ → bit = 0, leftover fraction = 0.50
	•	￼ → bit = 1, leftover fraction = 0.00
	•	So fractional bits = .101

Hence,
￼

8. Key Takeaways
	1.	Integer to Binary
	•	Repeatedly subtract the largest power of 2 (or do repeated integer‐divide by 2 & track remainders).
	•	Keep going down until nothing remains.
	2.	Fraction to Binary
	•	Multiply fractional part by 2; if ≥ 1, bit is 1 and subtract 1; else bit is 0.
	•	Repeat with leftover fraction.
	3.	Spreadsheets & Charts are simply ways to keep track of each step systematically:
	•	A row for each exponent (positive for the integer part, negative for the fraction).
	•	A column for “Does it fit (≥ or ≤)?” or “Remainder of dividing by 2?”
	4.	Leading Zeros for integer bits and trailing zeros for fractional bits are often not necessary unless you want a fixed “width” of bits.

9. Final “Visual” Recap

Below is a quick ASCII “diagram” summarizing the integer part approach by repeated division. Let’s say the integer is ￼. You keep dividing by 2:

   M
   ├─ remainder(LSB) = 0 or 1
   └─ M // 2 --> new M

Repeat until M = 0
Collect remainders in reverse order => binary

And for the fraction part ￼:

   F
   ├─ Multiply by 2 => x
   |   └─ if x >= 1 => bit = 1, leftover x-1
   |      else => bit = 0, leftover x
   └─ leftover becomes new F

Repeat until leftover = 0 or you have enough bits

That’s all there is to it!

By combining these two halves (integer + fraction) and systematically logging your steps with tables or charts, you can see exactly where each binary digit comes from.

Feel free to tweak the method you like best:
	•	“Powers of 2 Subtraction” or
	•	“Repeated Division for integer / Repeated Multiplication for fraction”

Both arrive at the same binary result.