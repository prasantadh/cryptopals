"""
Compute base64 encoded value of a string
@input:
    hexstring [string]: a hex string
@return:
    [bytes]: base64 encoded value of hexstring
"""
def hex2base64(hexstring):

    from base64 import b64encode
    return b64encode(bytes.fromhex(hexstring))

"""
Compute XOR combination of two equal length buffers
@input:
    x [string]: a hex string
    y [string]: a hex string
@return:
    [bytes]: character-wise XOR value of x and y in HEX
"""
def fixedXOR(x, y):

    assert len(x) == len(y), "Provided strings must be of equal length"
    return hex(int(x, 16) ^ int(y, 16))[2:]

"""
Compute XOR of a hex string and a single byte key
@input:
    hexstring [string]: a hex string
    key [int]: a single byte key to XOR the hexstring with
@return:
    [int]: score of the string
"""
def single_byte_xor(hexstring, key):
    assert type(key) == type(1), "key must be an integer"
    assert 0 <= key <= 255, "key must be between 0 and 255"

    ciphertext = bytes.fromhex(hexstring)
    plaintext = b''
    for i in range(len(ciphertext)):
        plaintext += bytes([ciphertext[i] ^ key])
    return plaintext

"""
Compute score of a text based on the sum of percentage-likelihood
of each of it's character appearing in an English text
@input:
    plaintext [string]: a string
@return:
    [int]: score of the string
"""
def frequency_score(plaintext):

    if type(plaintext) == type(b""):
        try:
            plaintext = plaintext.decode('utf8')
        except:
            return 0

    # from the wikipedia article on letter frequency
    weights = { 'a' :  8.167,  'b' : 1.492, 'c' : 2.782, 'd' : 4.253,
                'e' : 12.702,  'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
                'i' :  6.966,  'j' : 0.153, 'k' : 0.772, 'l' : 4.025,
                'm' :  2.406,  'n' : 6.749, 'o' : 7.507, 'p' : 1.929,
                'q' :  0.095,  'r' : 5.987, 's' : 6.327, 't' : 9.056,
                'u' :  2.758,  'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
                'y' :  1.974,  'z' : 0.074, ' ' : 15 }

    score = 0
    for char in plaintext.lower():
        if char in weights:
            score += weights[char]

    return score

