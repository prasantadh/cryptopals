from codecs import encode, decode
from struct import pack

def pad(ct, length):
    assert(length < 256)
    val = length - len(ct) % length
    val = val if val else length
    val = pack('B', val) * val
    return (ct + val)

def main():
    ct = b'YELLOW SUBMARINE'
    assert(pad(ct, 20) == b'YELLOW SUBMARINE\x04\x04\x04\x04')
    assert(pad(b'A' * 0x16, 0x16) == b'A' * 0x16 + b'\x16' * 0x16 )

if __name__ == '__main__':
    main()