# importing the script
import mea

# using the function
enc = mea.encrypt("Hello World")
print("Encrypted :", enc)
dec = mea.decrypt(enc)
print("Decrpyted :", dec)
