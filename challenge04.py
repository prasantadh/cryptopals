from cryptopals import helpers

with open('04.txt', 'r') as f:
    ciphertexts = f.readlines()

scores = []
for ciphertext in ciphertexts:
    ciphertext = bytes.fromhex(ciphertext)
    scores += helpers.brute_single_byte_xor(ciphertext)

# we could also make one pass and get the max
# this is safer
scores.sort(reverse=True)

for score in scores[:5]:
    print(score)
