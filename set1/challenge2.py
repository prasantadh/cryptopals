from codecs import encode, decode
from struct import pack

# get the hex
s1 = input('Enter the first hex: ')
s2 = input('Enter the second hex: ')

# assert correct input
assert(len(s1) == len(s2))
assert(len(s1) % 2 == 0)

# print out the results
print(hex(int(s1, 16) ^ int(s2, 16))[2:])