# IEEE-754 Floating-Point Worksheet - Worked Example

Number to Convert: -23.375₁₀

## Step 1: Sign Bit
[✓] Negative (1)
[ ] Positive (0)
Sign bit: 1

## Step 2: Convert to Binary
Integer part: 23₁₀ = 10111₂
Fraction part: 0.375₁₀ = 0.011₂
Combined: 10111.011₂

## Step 3: Normalize
1. Move decimal point to get 1.xxx format
   1.0111011 × 2⁴
2. Count positions moved: 4
   Direction: [✓] Right (+)

## Step 4: Calculate Exponent (32-bit format)
1. Bias: 127
2. True exponent: +4
3. Biased exponent: 127 + 4 = 131
4. Binary exponent: 131₁₀ = 10000011₂

## Step 5: Mantissa
1. Drop leading 1
2. Pad with zeros if needed
Mantissa: 01110110000000000000000

## Final Assembly (32-bit)
[✓] 32-bit (1+8+23)
[ ] 64-bit (1+11+52)

|  Sign  |  Exponent  |        Mantissa        |
|--------|------------|------------------------|
|   1    | 10000011  | 01110110000000000000000|

Hex: 0xC1BB0000

Verification:
- Sign: Negative
- Exponent: 131 - 127 = 4
- Mantissa: 1.0111011 × 2⁴ = 10111.011₂ = -23.375₁₀ 