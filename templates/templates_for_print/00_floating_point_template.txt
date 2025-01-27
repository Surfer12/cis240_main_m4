# IEEE-754 Floating-Point Worksheet - Example Template

## Problem Statement
Number to Convert: _______₁₀

## Step 1: Sign Bit
[ ] Negative (1)
[ ] Positive (0)
Sign bit: _______

## Step 2: Convert to Binary
Integer part: _______₁₀ = _______₂
Fraction part: _______₁₀ = _______₂
Combined: _______₂

## Step 3: Normalize
1. Move decimal point to get 1.xxx format
   _______ × 2^_______
2. Count positions moved: _______
   Direction: [ ] Left (-) [ ] Right (+)

## Step 4: Calculate Exponent
1. Bias: [ ] 127 (32-bit) [ ] 1023 (64-bit)
2. True exponent: _______
3. Biased exponent: _______ + _______ = _______
4. Binary exponent: _______₁₀ = _______₂

## Step 5: Mantissa
1. Drop leading 1
2. Pad with zeros if needed
Mantissa: _______

## Final Assembly
[ ] 32-bit (1+8+23)
[ ] 64-bit (1+11+52)

|  Sign  |  Exponent  |        Mantissa        |
|--------|------------|------------------------|
|   _    | ________  | ____________________|

## Verification
- Sign: _______
- Exponent: _______ - _______ = _______
- Mantissa: _______ × 2^_______ = _______₂ = _______₁₀

## Common Pitfalls
1. Forgetting to subtract bias
2. Including leading 1 in mantissa
3. Incorrect direction for exponent
4. Not padding mantissa with zeros

Final Answer: 0x_______ 