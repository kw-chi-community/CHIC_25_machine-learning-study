from icecream import ic

def binary_to_float(binary_list):
    bits = 0
    for bit in binary_list:
        bits = (bits << 1) | bit
    
    sign = bits >> 31
    
    exponent = (bits >> 23) & 0xFF
    
    mantissa = bits & 0x7FFFFF
    
    if exponent == 0:
        if mantissa == 0:
            return 0.0
        exponent = -126
        mantissa = mantissa / 0x800000
    else:
        exponent -= 127
        mantissa = (mantissa | 0x800000) / 0x800000
    
    result = mantissa * (2.0 ** exponent)
    return -result if sign else result

if __name__ == "__main__":
    binary = [0,
          1,0,0,0,0,0,0,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    result = binary_to_float(binary)
    ic(result)