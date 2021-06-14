from cryptopals import helpers

plaintext = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

ciphertext = helpers.encrypt_w_repeated_xor(plaintext,key)
from codecs import encode
print(encode(ciphertext, 'hex'))
