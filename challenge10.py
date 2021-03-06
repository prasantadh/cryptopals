from cryptopals import helpers
from codecs import encode, decode
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES

def main():

    # prepare the ciphertext
    with open('10.txt', 'r') as f:
        ct = f.read().replace('\n', '')
    ct = decode(bytes(ct, 'utf-8'), 'base64')
    assert(len(ct) % 16 == 0)

    # prepare the cipher
    IV = b'\x00' * 16
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)

    # decrypt CBC mode with ECB cipher
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    pt = b''
    for block in blocks:
        pt += strxor(cipher.decrypt(block), IV)
        IV = block
    print(pt.decode('utf-8'))


if __name__ == '__main__':
    main()
