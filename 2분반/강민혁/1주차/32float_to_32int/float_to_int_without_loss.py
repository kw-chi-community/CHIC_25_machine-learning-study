from icecream import ic

def convert_without_loss(binary):
    sign = -1 if binary[0] == 1 else 1
    
    exponent = 0
    for i in range(1, 9):
        exponent = (exponent << 1) | binary[i]
    exponent -= 127  
    
    mantissa = 0
    for i in range(9, 32):
        mantissa = (mantissa << 1) | binary[i]
    mantissa = (1 << 23) | mantissa
    
    if exponent < 0:
        result = mantissa >> (-exponent)
    else:
        result = mantissa << exponent
    
    return sign * result


if __name__ == "__main__":
    import binary_to_float, float_to_binary

    binary = float_to_binary.float_to_binary(3.141592025756836)

    # binary = [0,
    #       1,0,0,0,0,0,0,
    #       1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    btf = binary_to_float.binary_to_float(binary)
    ic(btf)
    
    result = convert_without_loss(binary)
    ic(result)