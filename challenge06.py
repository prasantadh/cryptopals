from cryptopals import helpers

NKEYS = 3           # number of keysizes to try # currently disabled
KEYSIZE_MIN = 2     # minimum key length to guess
KEYSIZE_MAX = 40    # maximum key length to guess

assert helpers.edit_distance('this is a test', 'wokka wokka!!!') == 37, "Oops!"

with open('06.txt', 'rb') as f:
    ciphertext = f.read().strip()
from base64 import b64decode
ciphertext = b64decode(ciphertext)

# finding the keysize
keysizes = []
for keysize in range(KEYSIZE_MIN, KEYSIZE_MAX + 1):
    distance = 0
    for i in range(0, 20):
        distance += helpers.edit_distance(
                        ciphertext[i*keysize:(i+1)*keysize],
                        ciphertext[(i+1)*keysize:(i+2)*keysize]
                        ) / keysize
    keysizes.append((distance, keysize))
keysizes.sort()
keysize = min(keysizes)[1]

# transposing into blocks
blocks = [''] * keysize
for i in range(keysize):
    blocks[i] = ciphertext[i::keysize]

# contructing the key, one byte at a time
key = ''
for i in range(len(blocks)):
    key += chr(helpers.brute_single_byte_xor(blocks[i], 1)[0][2])

plaintext = helpers.decrypt_w_repeated_xor(ciphertext, key)
print(plaintext.decode())
