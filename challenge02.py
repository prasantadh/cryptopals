from Crypto.Util.strxor import strxor
from codecs import encode, decode

"""
s1 = input('Enter the first hex: ')
s2 = input('Enter the second hex: ')
s1 = decode(s1, 'hex')
s2 = decode(s2, 'hex')
ans = strxor(s1, s2).hex()
# alternatively,
# ans = hex(int(s1, 16) ^ int(s2, 16))[2:]
print(ans)
"""

from cryptopals import helpers
ct1 = "1c0111001f010100061a024b53535009181c"
ct2 = "686974207468652062756c6c277320657965"
print(helpers.fixedXOR(ct1, ct2))

