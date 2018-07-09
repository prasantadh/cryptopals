from codecs import encode, decode
from Crypto.Util.strxor import strxor

def repeated_key_xor(pt, key):
    key = key * (len(pt) // len(key)) + b'ICE'[:(len(pt) % len(key))]
    return strxor(pt, key)

def main():
    pt = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = b'ICE'
    print(encode(repeated_key_xor(pt, key), 'hex'))

if __name__ == '__main__':
    main()
