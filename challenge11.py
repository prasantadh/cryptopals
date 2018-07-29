from codecs import encode, decode
from Crypto.Cipher import AES
from random import randint
from os import urandom 
from challenge9 import pad

def detect_mode(ct):
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    return 'ECB' if len(blocks) != len(set(blocks)) else 'CBC'

def encryption_oracle(pt):
    pt = urandom(randint(5,10)) + pt + urandom(randint(5, 10))
    pt = pad(pt, (len(pt) // 16 + 1) * 16) if len(pt) % 16 else pt
    key = urandom(16)
    if randint(0, 1):
        print('encrypted with ECB. ', end='')
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        print('encrypted with CBC. ', end='')
        cipher = AES.new(key, AES.MODE_CBC, urandom(16))
    return cipher.encrypt(pt)

def main():
    pt = b's'*30
    ct = encryption_oracle(pt)
    print('detected', detect_mode(ct))
    return 0

if __name__ == '__main__':
    main()