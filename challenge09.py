from cryptopals import helpers

def main():
    ct = b'YELLOW SUBMARINE'
    assert(helpers.pad(ct, 20) == b'YELLOW SUBMARINE\x04\x04\x04\x04')
    assert(helpers.pad(b'A' * 0x16, 0x16) == b'A' * 0x16 + b'\x16' * 0x16 )
    print('passed the tests')

if __name__ == '__main__':
    main()
