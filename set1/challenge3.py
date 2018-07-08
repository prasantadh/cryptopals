from codecs import encode, decode
from Crypto.Util.strxor import strxor_c

def single_byte_xor(ct):
    score = lambda s: sum([1 for c in s.lower() if c in b'etaoin '])
    return max([strxor_c(ct, k) for k in range(256)], key=score)

def main():
    ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ct = decode(ct, 'hex')
    print(single_byte_xor(ct).hex())


if __name__ == '__main__':
    main()
