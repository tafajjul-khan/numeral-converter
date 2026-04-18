
def dec_to_any_base(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if(base > len(digits)):
        print("Base is bigger than digits")
        return
    
    int_part = int(num)
    fract_part = num - int_part

    res_int = ""
    if(int_part == 0):
        res_int = "0"
    
    while int_part > 0:
        remainder = int_part % base
        res_int = digits[remainder] + res_int
        int_part //= base

    res_fract = ""
    if fract_part > 0:
        res_fract = "."
        precision = 5
        for _ in range(precision):
            fract_part *= base
            digit = int(fract_part)
            res_fract += digits[digit]
            fract_part -= digit
            if fract_part == 0:
                break

    return res_int + res_fract


def any_base_to_decimal(num_str, base):
    
    digits_lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
   
    if base < 2 or base > 36:
        return "Base between 2 to 36."

    
    if "." in num_str:
        int_part_str, fract_part_str = num_str.split(".")
    else:
        int_part_str, fract_part_str = num_str, ""

    
    res_int = 0
    power = 0
    
    for char in reversed(int_part_str.upper()):
        digit = digits_lookup.find(char)
        
       
        if digit == -1 or digit >= base:
            return f"'{char}' not valid for {base}"
            
        res_int += digit * (base ** power)
        power += 1

   
    res_fract = 0.0
    power = -1
    for char in fract_part_str.upper():
        digit = digits_lookup.find(char)
        
        if digit == -1 or digit >= base:
            return f"'{char}' not valid for {base}"
            
        res_fract += digit * (base ** power)
        power -= 1

    return res_int + res_fract



def convert_any_to_any(num_str, from_base, to_base):
    try:
        # Step 1: Check bases same 
        if from_base == to_base:
            return num_str
        
        # Step 2: Source Base -> Decimal
        decimal_val = any_base_to_decimal(num_str, from_base)
        
        # Step 3: Decimal -> Target Base
        final_result = dec_to_any_base(decimal_val, to_base)
        
        return final_result
    except Exception as e:
        return f"Error: {e}"

print("Binary '1010.101' to Hex:", convert_any_to_any("1010.101", 2, 16)) 
print("Hex 'A' to Octal:", convert_any_to_any("A", 16, 8))               
print("Decimal '15' to Binary:", convert_any_to_any("15", 10, 2))

