from cryptopals import helpers

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# xor with each possible value of a byte
# get the frequency score of the decoded plaintext
# sort by the largest score first
scores = []
for key in range(255):
    plaintext = helpers.single_byte_xor(ciphertext, key)
    score = helpers.frequency_score(plaintext)
    scores.append((score, plaintext, key))
scores.sort(reverse=True)

for score in scores[:5]:
    print(score)
