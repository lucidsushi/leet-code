a = 9
b = 2

def int_to_binary(n):
    return bin(n)[2:].zfill(8)

def binary_to_int(n):
    return int(n, 2)

# print(int_to_binary(a))
# print(int_to_binary(b))
# print(binary_to_int('1011'))
# print(a | b)

def learn_bitwise():
    a = 5
    b = 6
    print(f'{a} & (AND) {b}\n{int_to_binary(a)}\n{int_to_binary(b)}\n{int_to_binary(a & b)}\n{a & b} \n')
    print(f'{a} | (OR) {b}\n{int_to_binary(a)}\n{int_to_binary(b)}\n{int_to_binary(a | b)}\n{a | b} \n')
    print(f'{a} ^ (XOR) {b}\n{int_to_binary(a)}\n{int_to_binary(b)}\n{int_to_binary(a ^ b)}\n{a ^ b} \n')
    print(f'{a} >> (Right Shift) {b}\n{int_to_binary(a)}\n{int_to_binary(b)}\n{int_to_binary(a >> 0)}\n{a >> 0} \n')
    print(f'{a} << (Left Shift) {b}\n{int_to_binary(a)}\n{int_to_binary(b)}\n{int_to_binary(a << 0)}\n{a << 0} \n')

# learn_bitwise()


# when to use xor in bitwise
# 1. when you want to check if two numbers are different

# when to use and in bitwise
# 1. when you want to check if two numbers are same

# when to use or in bitwise
# 1. when you want to check if one of the numbers is 1

# when to use right shift in bitwise
# 1. when you want to move the bits to right

# what does moving bits affect a number?
# 1. when you move bits to right, the number will be divided by 2
# 2. when you move bits to left, the number will be multiplied by 2
