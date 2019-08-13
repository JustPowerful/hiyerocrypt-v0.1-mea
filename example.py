from mea import MEA
from mea import LIST

mea = MEA()
lst = LIST()

# returns a encrypted or a decrypted list
# CAPS ARE NOT SUPPORTED (Bug)
enclist = lst.enlist("hello world")
declist = lst.delist("208 202 216 216 222 64 238 222 228 216 200") # don't forget to add the space between every ascii

# returns an encrypted or a decrpyted string
encstring = mea.encrypt("hello world")
decstring = mea.decrypt(encstring)
