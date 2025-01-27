# Hexadecimal Conversion Worksheet - Worked Example

## Quick Reference Table
| Hex | Binary | Decimal |  | Hex | Binary | Decimal |
|-----|---------|---------|--|-----|---------|---------|
| 0   | 0000    | 0       |  | 8   | 1000    | 8       |
| 1   | 0001    | 1       |  | 9   | 1001    | 9       |
| 2   | 0010    | 2       |  | A   | 1010    | 10      |
| 3   | 0011    | 3       |  | B   | 1011    | 11      |
| 4   | 0100    | 4       |  | C   | 1100    | 12      |
| 5   | 0101    | 5       |  | D   | 1101    | 13      |
| 6   | 0110    | 6       |  | E   | 1110    | 14      |
| 7   | 0111    | 7       |  | F   | 1111    | 15      |

## Conversion Steps
Starting Number: 173₁₀ Base: Decimal → Hex

### Method 1: Through Binary
Step 1: Convert to binary first
173₁₀ = 10101101₂ (by division by 2 method)

Step 2: Group bits by 4 (pad left with zeros if needed)
Binary: 1010 1101

Step 3: Convert each group using table
Group 1: 1010 → A
Group 2: 1101 → D

### Method 2: Direct Division (Dec → Hex)
Divisions by 16:
1. 173 ÷ 16 = 10 R 13 (D)
2. 10 ÷ 16 = 0 R 10 (A)

Final Answer: 0xAD
Verification: AD₁₆ = 10101101₂ = 173₁₀ 