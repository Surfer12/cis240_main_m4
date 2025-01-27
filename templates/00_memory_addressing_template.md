# Memory Addressing Worksheet - Example Template

## Address Calculation
Base Address: 0x_______
Offset: 0x_______
Data Size: _______ bytes

### Direct Addressing
Final Address = Base + Offset
Calculation: 0x_______ + 0x_______ = 0x_______

### Indexed Addressing
Index Register: _______
Scale Factor: _______ (for _______-byte elements)
Final Address = Base + (Index × Scale) + Offset
Calculation: _______ + (_______ × _______) + _______ = _______

### Array Access
Array Base: 0x_______
Element Size: _______ bytes
Index: _______
Address = Base + (Index × Size)
Calculation: _______ + (_______ × _______) = _______

## Alignment Check
[ ] Byte aligned (any address)
[ ] Word aligned (divisible by 2)
[ ] Double-word aligned (divisible by 4)
[ ] Cache line aligned (divisible by 64)

Show alignment calculation:
Address: 0x_______
Divisible by _______: _______ remainder _______

## Page Translation
Virtual Address: 0x_______
Page Size: _______ bytes (0x_______)

### Page Number Calculation
Page Number = VA ÷ Page Size
Calculation: 0x_______ ÷ 0x_______ = 0x_______

### Page Offset Calculation
Page Offset = VA % Page Size
Calculation: 0x_______ % 0x_______ = 0x_______

## Verification
[ ] All addresses within valid range
[ ] Alignment requirements met
[ ] Page calculations correct

## Common Pitfalls
1. Forgetting to account for data size
2. Incorrect alignment calculations
3. Mixing decimal and hex calculations

Final Physical Address: 0x_______ 