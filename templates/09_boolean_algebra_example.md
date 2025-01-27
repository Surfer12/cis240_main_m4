# Boolean Algebra and Logic Gates Worksheet - Worked Example

## Truth Table Construction
Expression: F = (A·B)' + (B·C)

| A | B | C | (A·B) | (A·B)' | (B·C) | Result |
|---|---|---|-------|--------|-------|---------|
| 0 | 0 | 0 |   0   |   1    |   0   |    1    |
| 0 | 0 | 1 |   0   |   1    |   0   |    1    |
| 0 | 1 | 0 |   0   |   1    |   0   |    1    |
| 0 | 1 | 1 |   0   |   1    |   1   |    1    |
| 1 | 0 | 0 |   0   |   1    |   0   |    1    |
| 1 | 0 | 1 |   0   |   1    |   0   |    1    |
| 1 | 1 | 0 |   1   |   0    |   0   |    0    |
| 1 | 1 | 1 |   1   |   0    |   1   |    1    |

## Boolean Expression Simplification
Original: F = (A·B)' + (B·C)

### Step 1: Apply Laws
1. DeMorgan's Law: (A·B)' = A' + B'
2. Distributive: F = (A' + B') + (B·C)
3. Associative: F = A' + B' + (B·C)

### Step 2: Karnaugh Map
```
    BC
AB  00 01 11 10
00  1  1  1  1
01  1  1  1  1
11  1  1  1  0
```

### Step 3: Circuit Implementation
Original Circuit:
```
A ---[AND]--[NOT]--[OR]--- F
B ---[AND]----/
     |
C ---[AND]----/
```

Simplified Circuit:
```
A'---[OR]--- F
B'---[OR]--/
B ---[AND]-/
C ---[AND]/
```

Gate Count: 
- Original: 4 gates (2 AND, 1 NOT, 1 OR)
- Simplified: 4 gates (1 AND, 2 NOT, 1 OR)
Maximum Delay: 3 gate delays

Final Simplified Expression: F = A' + B' + (B·C) 