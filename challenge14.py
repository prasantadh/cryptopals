from codecs import encode, decode
from struct import pack
from os import urandom
from random import randint
from challenge12 import oracle as c12oracle
import sys

### server side routines
def oracle(pt):
    prefixsize = randint(2, 5)
    return c12oracle(urandom(prefixsize) + pt)

### attacker side routines
def find_blocksize():
    sizes = set([len(oracle(b'A' * i)) for i in range(40)])
    sizes = sorted(list(sizes))[:2]
    return abs(sizes[0] - sizes[1])

def find_start_idx(ct, blocksize):
    for i in range(blocksize, len(ct), blocksize):
        if ct[i-blocksize:i] == ct[i:i+blocksize]:
            return i + blocksize
    return 0

def find_prefixsize(blocksize):
    pool = []
    for size in range(2 * blocksize, 3 * blocksize):
        padding = b'A' * size
        for _ in range(blocksize * blocksize):
            sample_ct = oracle(padding)
            pool += [(find_start_idx(sample_ct, blocksize), size, len(sample_ct))]
    return min([p for p in pool if p[0] != 0])

def break_AES_ECB():
    blocksize = find_blocksize()
    start_idx, prefixsize, len_ct = find_prefixsize(blocksize)
    print(start_idx, prefixsize, len_ct)
    assert(start_idx)
    pt = b''
    for _ in range(len_ct):
        reference = {}
        guess = b'\xAA' * prefixsize 
        guess += urandom(len_ct - start_idx - len(pt) - 1) 
        for b in [10] + list(range(32, 127)):
            sample_ct = oracle(guess + pt + pack('B', b))
            while(find_start_idx(sample_ct, blocksize) != start_idx): 
                sample_ct = oracle(guess + pt + pack('B', b))
            reference[guess + pt + pack('B', b)] = sample_ct[start_idx:len_ct]
        sample_ct = oracle(guess)
        while(find_start_idx(sample_ct, blocksize) != start_idx): 
            sample_ct = oracle(guess)
        decrypting = False
        i = 0
        for k, v in reference.items():
            i = i + 1
            if v == sample_ct[start_idx:len_ct]:
                pt += k[-1:]
                decrypting = True
        if not decrypting: return pt


def main():
    print(break_AES_ECB())

if __name__=='__main__':
    main()