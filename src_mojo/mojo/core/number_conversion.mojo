fn single_conversion_to_and_fro(value: Float) -> str:
    return float_to_ieee754(value)

fn main():
    float_value = -123.456
    ieee754_representation = single_conversion_to_and_fro(float_value)
    print(f"IEEE 754 representation of {float_value}: {ieee754_representation}") 