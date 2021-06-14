# just look for duplicate section of 16 bytes

with open('08.txt', 'rb') as f:
    ciphertexts = f.readlines()
    ciphertexts = [line.strip() for line in ciphertexts]

for ciphertext in ciphertexts:
    blocks = []
    for i in range(0, len(ciphertext), 32):
        blocks.append(ciphertext[i:i+32])

    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if blocks[i] == blocks[j]:
                print("Found a match: ", blocks[i], blocks[j])
                print("Full ciphertext: ", ciphertext)
                exit(0)

