from struct import pack

def stripPKCS(pt):
    assert(len(pt) % 16 == 0) # the problem specification
    l = min(16 + 1, len(pt))# scheme well-defined for N < 256
    for i in range(1, l):
        if pt[-i:] == pack('B', i) * i:
            return pt[:-i]
    raise ValueError('Not a valid PKCS padding')

def main():
    assert(stripPKCS(b'A'*16 + b'\x10'*16) == b'A' * 16)
    assert(stripPKCS(b'A'*10 + b'\x06'* 6) == b'A' * 10)

if __name__ == '__main__':
    main()