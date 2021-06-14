from cryptopals import helpers
from codecs import decode

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ciphertext = bytes.fromhex(ciphertext)

for score in helpers.brute_single_byte_xor(ciphertext):
    print(score)
