from icecream import ic
import struct

def float_to_binary(num):
    bits = struct.unpack('I', struct.pack('f', num))[0]
    
    binary = []
    for i in range(31, -1, -1):
        bit = (bits >> i) & 1
        binary.append(bit)
    
    return binary

if __name__ == "__main__":
    test_num = 3.141592025756836
    result = float_to_binary(test_num)
    ic(result)


    from binary_to_float import binary_to_float
    btf = binary_to_float(result)
    ic(btf) 
