from codecs import encode, decode
from Crypto.Cipher import AES

def main():
    with open('07.txt', 'r') as f:
        ct = f.read().replace('\n', '')
    while (len(ct) % 16): ct += '.'
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    ct = decode(bytes(ct, 'utf-8'), 'base64')
    print(cipher.decrypt(ct).decode('utf-8'))

if __name__=='__main__':
    main()
