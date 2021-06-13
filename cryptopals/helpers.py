"""
@input:
    hexstring:
        class: 'bytes'
        description: a hex string
@return:
    class: 'bytes'
    description: base64 encoded value of hexstring
"""
def hex2base64(hexstring):
    from base64 import b64encode
    return b64encode(bytes.fromhex(hexstring))
