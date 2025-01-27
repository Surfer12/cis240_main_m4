# Memory Addressing Worksheet - Worked Example

## Address Calculation
Base Address: 0x1000
Offset: 0x24
Data Size: 4 bytes

### Direct Addressing
Final Address = Base + Offset
Calculation: 0x1000 + 0x24 = 0x1024

### Indexed Addressing
Index Register: 3
Scale Factor: 4 (for 4-byte elements)
Final Address = Base + (Index × Scale) + Offset
Calculation: 0x1000 + (3 × 4) + 0x24 = 0x1030

### Array Access
Array Base: 0x2000
Element Size: 8 bytes (double)
Index: 5
Address = Base + (Index × Size)
Calculation: 0x2000 + (5 × 8) = 0x2028

## Alignment Check
[ ] Byte aligned
[ ] Word aligned (2 bytes)
[✓] Double-word aligned (4 bytes)
[ ] Cache line aligned (64 bytes)

Explanation: 0x1024 is divisible by 4, making it double-word aligned

## Page Translation
Virtual Address: 0x12345678
Page Size: 4096 bytes (0x1000)
Page Number = VA ÷ Page Size = 0x12345
Page Offset = VA % Page Size = 0x678

Verification:
- Page Number × Page Size + Offset = Virtual Address
- 0x12345 × 0x1000 + 0x678 = 0x12345678 