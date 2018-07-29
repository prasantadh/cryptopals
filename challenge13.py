from Crypto.Cipher import AES
from random import randint
from struct import pack
from os import urandom
from challenge9 import pad

key = urandom(16)

def parse(cookie):
    args = cookie.split('&')
    obj = {}
    for arg in args:
        temp = arg.split('=')
        obj[temp[0]] = temp[1]
    return obj

def profile_for(addr):
    assert(addr.find('=') == -1)
    assert(addr.find('&') == -1)
    if (addr == 'admin'):
        return {'email': 'admin@m.e', 'uid': 0, 'role': 'admin'}
    return {'email': addr, 'uid': str(randint(1, 65000)), 'role': 'user'}

def encrypt(profile):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = b''
    for k,v in profile.items():
        pt += bytes(k, 'utf-8') + b'=' + bytes(v, 'utf-8') + b'&'
    pt = pt[:-1]
    pt = pad(pt, (len(pt) // 16 + 1) * 16)
    return cipher.encrypt(pt)

def decrypt(profile):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(profile)
    for n in range(len(pt), 0, -1):
        if pt[-n:] == pack('B', n) * n:
            pt = pt[:-n]
            break
    return pt
    
def main():
    print(parse('user=user&id=10&role=user'))
    print(profile_for('user@user.com'))
    print(encrypt(profile_for('u@u.com')))
    print(decrypt(encrypt(profile_for('u@u.com'))))


if __name__ == '__main__':
    main()