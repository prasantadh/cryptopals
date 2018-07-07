from codecs import encode, decode
from Crypto.Util.strxor import strxor_c
# ETAOIN
def score(table):
    ans = 0
    for s in 'ETAOINetaoin':
        if s in table.keys():
            ans += table[s]
    return ans

def find_key(ct):
    max_score = 0
    for k in range(127):
        table = {}
        for b in ct:
            if chr(k ^ b) in table:
                table[chr(k ^ b)] += 1
            else:
                table[chr(k ^ b)] = 1
        if score(table) > max_score:
            max_score, key = score(table), k
    return key
    
def decrypt(key, ct):
    pt = ''
    for c in ct:
        pt += chr(c ^ key)
    return pt

def main():
    ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ct = decode(ct, 'hex')
    print(decrypt(find_key(ct), ct))


if __name__ == '__main__':
    main()
