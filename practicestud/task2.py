def any_to_str(n):
    if n == 0: return "0"
    res, digits = "", "0123456789"
    sign = "-" if n < 0 else ""
    n = abs(n)
    
    i_part = int(n)
    f_part = n - i_part
    
    s_int = ""
    if i_part == 0: s_int = "0"
    while i_part > 0:
        s_int = digits[i_part % 10] + s_int
        i_part //= 10
        
    s_float = ""
    if f_part > 0:
        s_float = "."
        for _ in range(5):
            f_part *= 10
            d = int(f_part)
            s_float += digits[d]
            f_part -= d
            if f_part == 0: break
            
    return sign + s_int + s_float

f_num = 15.5
f_num_neg = -0.77

print(f"Input: {f_num} -> Output: '{any_to_str(f_num)}'")
print(f"Input: {f_num_neg} -> Output: '{any_to_str(f_num_neg)}'")
