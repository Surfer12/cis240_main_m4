def create_table():
    print("| 2^n | Decimal Value |")
    print("|-----|---------------|")
    for i in range(10):
        decimal_value = 2 ** i
        print(f"| 2^{i} | {decimal_value} |")

create_table()