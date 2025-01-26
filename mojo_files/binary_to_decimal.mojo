func binary_to_decimal(binary_num: String) -> Int {
    return Int(binary_num, radix: 2)!
}

let binary_num = "101101"
let decimal_num = binary_to_decimal(binary_num)
print("The decimal representation of \(binary_num) is \(decimal_num)")