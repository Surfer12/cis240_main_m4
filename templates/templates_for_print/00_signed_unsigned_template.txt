# Signed vs Unsigned Comparison Worksheet - Example Template

## Number Analysis
Binary: _______₂
Bit width: _______ bits

### Unsigned Interpretation
Value: _______₁₀
Range: 0 to 2^n-1 (0 to _______)

### Signed Interpretation (Two's Complement)
MSB: _______ (0=positive, 1=negative)
If negative, two's complement steps:
1. Invert bits: _______
2. Add 1: _______
Value: _______₁₀
Range: -2^(n-1) to 2^(n-1)-1 (_______ to _______)

## Comparison Operations
Compare with: _______₂ (_______₁₀)

### Unsigned Comparison
[ ] Greater than
[ ] Less than
[ ] Equal to
Result: _______ ⊕ _______

### Signed Comparison
[ ] Greater than
[ ] Less than
[ ] Equal to
Result: _______ ⊕ _______

## Overflow/Underflow Check
Operation: _______
Show work:
_______
_______
_______

### Unsigned Check
[ ] No overflow (result ≤ maximum unsigned value)
[ ] Overflow occurs

### Signed Check
[ ] No overflow (result within signed range)
[ ] Overflow occurs

## Common Pitfalls
1. Forgetting to check MSB for signed numbers
2. Using wrong comparison for signed vs unsigned
3. Not considering full range for overflow

## Final Notes
- Same bits can represent different values
- Signed range is asymmetric
- Overflow conditions differ for signed/unsigned 