from codecs import encode, decode
from Crypto.Util.strxor import strxor
from struct import pack, unpack
from challenge3 import single_byte_xor
from challenge5 import repeated_key_xor

#number of keys to extract
nkeys = 1
keysize_min = 2
keysize_max = 40

def edit_distance(a, b):
    n1 = lambda i : sum((i & (1 << j)) != 0 for j in range(7))
    return sum([n1(c) for c in strxor(a, b)])

def find_keysize(ct):
    ans = []
    for keysize in range(keysize_min, keysize_max):
        blocks = [ct[i:i+keysize] for i in range(0, keysize*10, keysize)]
        pairs  = [(blocks[i], blocks[j]) for i in range(len(blocks))\
                 for j in range(i+1, len(blocks))]
        dists  = [edit_distance(pair[0], pair[1]) for pair in pairs]
        ans    += [(sum(dists) / keysize, keysize)]
    return [p[1] for p in sorted(ans)[:nkeys]]

def getKey(keysize, ct):
    key = b''
    for i in range(keysize):
        block = ct[i:len(ct):keysize]
        key += single_byte_xor(block)['key']
    return key

def main():
    assert (edit_distance(b'this is a test', b'wokka wokka!!!') == 37)
    with open('6.txt', 'r') as f:
        ct = f.read().replace('\n', '')
    ct = decode(bytes(ct, 'utf-8'), 'base64')
    for keysize in find_keysize(ct):
        key = getKey(keysize, ct)
        pt  = repeated_key_xor(ct, key)
        print(key.decode('utf-8'))
        print(pt.decode('utf-8'))

if __name__ == '__main__':
    main()
