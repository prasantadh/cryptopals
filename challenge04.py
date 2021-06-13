from cryptopals import helpers

with open('4.txt', 'r') as f:
    lines = f.readlines()

scores = []
for line in lines:
    for key in range(256):
        plaintext = helpers.single_byte_xor(line, key)
        score = helpers.frequency_score(plaintext)
        if score != 0:
            scores.append((score, plaintext, key))

# we could also make one pass and get the max
# this is safer
scores.sort(reverse=True)

for score in scores[:5]:
    print(score)
