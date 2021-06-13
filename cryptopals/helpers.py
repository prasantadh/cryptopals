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
Take two equal length buffers and produce their XOR combination
@input:
    x [string]: a hex string
    y [string]: a hex string
@return:
    [bytes]: character-wise XOR value of x and y in HEX
"""
def fixedXOR(x, y):

    assert len(x) == len(y), "Provided strings must be of equal length"
    return hex(int(x, 16) ^ int(y, 16))[2:]


