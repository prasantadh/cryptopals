from codecs import encode, decode
from challenge3 import single_byte_xor

def main():
    with open('4.txt', 'r') as f:
        lines = f.readlines()
    lines = [bytes.fromhex(line.strip()) for line in lines ]
    pt = max([single_byte_xor(line) for line in lines], key=lambda t: t['score'])
    print(pt['pt'].strip().decode('utf-8'))

if __name__ == '__main__':
    main()