from cryptopals import helpers
ct1 = "1c0111001f010100061a024b53535009181c"
ct2 = "686974207468652062756c6c277320657965"
print(helpers.fixedXOR(ct1, ct2))

