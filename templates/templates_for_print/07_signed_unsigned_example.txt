# Signed vs Unsigned Comparison Worksheet - Worked Example

## Number Analysis
Binary: 11010110₂
Bit width: 8 bits

### Unsigned Interpretation
Value: 214₁₀
Range: 0 to 2⁸-1 (0 to 255)

### Signed Interpretation (Two's Complement)
MSB: 1 (negative)
Value: -42₁₀ (found by taking two's complement)
Range: -2⁷ to 2⁷-1 (-128 to 127)

## Comparison Operations
Compare with: 00101010₂ (42₁₀)

### Unsigned Comparison
[✓] Greater than
[ ] Less than
[ ] Equal to
Result: 214 > 42

### Signed Comparison
[ ] Greater than
[✓] Less than
[ ] Equal to
Result: -42 < 42

## Overflow/Underflow Check
Operation: Addition with 00001111₂ (15₁₀)

Unsigned:
11010110₂ + 00001111₂ = 11100101₂ (229₁₀)
[✓] No unsigned overflow (229 < 255)

Signed:
-42₁₀ + 15₁₀ = -27₁₀
[ ] No signed overflow (result within -128 to 127)

Note: This example demonstrates how the same bit pattern (11010110₂) represents different values depending on whether it's interpreted as signed (-42₁₀) or unsigned (214₁₀). 