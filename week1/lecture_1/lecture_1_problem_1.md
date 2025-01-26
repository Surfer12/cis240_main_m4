Convert 0101 base 2 to base 10. 

0 \ 1 \ 0 \ 1 >

(0 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 0 + 4 + 0 + 1 = 5


Convert 0101.01 base 2 to base 10.

0 \ 1 \ 0 \ 1 \ . \ 0 \ 1 >

(0 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) + (0 * 2^-1) + (1 * 2^-2) = 0 + 4 + 0 + 1/4 + 0 + 0.25 = 5.25




`| Power | Value |` and `|---|---|`.
2. Iterate through the list of powers of 2
3. For each power, extract the exponent and the value.
4. Create a table row in markdown format: `| exponent | value |`.
5. Combine the header and rows to form the complete markdown table.
``` 
| Power | Value |
|---|---|
| 2^0 | 1 |
| 2^1 | 2 |
| 2^2 | 4 |
| 2^3 | 8 |
| 2^4 | 16 |
| 2^5 | 32 |
| 2^6 | 64 |
| 2^7 | 128 |
| 2^8 | 256 |
| 2^9 | 512 |
| 2^10 | 1024 |
```
