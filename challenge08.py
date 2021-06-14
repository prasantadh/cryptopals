from codecs import encode, decode

def main():
    with open('8.txt', 'r') as f:
        ct = f.readlines()
    ct = [decode(bytes(t.strip(), 'utf-8'), 'base64') for t in ct]
    blocks = lambda t : [t[i:i+16] for i in range(0, len(t), 16)]
    has_duplicates = lambda l: len(l) != len(set(l)) 
    ans = [t for t in ct if has_duplicates(blocks(t))][0]
    for block in blocks(ans):
        print(encode(block, 'hex'))

if __name__=='__main__':
    main()