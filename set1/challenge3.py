from codecs import encode, decode
from Crypto.Util.strxor import strxor_c

# from the wikipedia article on letter frequency
weight = {  'a' :  8.167,  'b' : 1.492, 'c' : 2.782, 'd' : 4.253,
            'e' : 12.702,  'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
            'i' :  6.966,  'j' : 0.153, 'k' : 0.772, 'l' : 4.025,
            'm' :  2.406,  'n' : 6.749, 'o' : 7.507, 'p' : 1.929,
            'q' :  0.095,  'r' : 5.987, 's' : 6.327, 't' : 9.056,
            'u' :  2.758,  'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
            'y' :  1.974,  'z' : 0.074, ' ' : 15 }

def single_byte_xor(ct):
    score = lambda s: sum([weight[chr(c)] for c in s.lower() if chr(c) in weight.keys()])
    pt =  max([strxor_c(ct, k) for k in range(256)], key=score)
    return {'key' : ct[0] ^ pt[0], 'pt' : pt, 'score': score(pt)}

def main():
    ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ct = decode(ct, 'hex')
    print(single_byte_xor(ct))

if __name__ == '__main__':
    main()
