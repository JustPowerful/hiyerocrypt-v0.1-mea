# importing the script
import functions as fn

# using the function
enc = fn.encrypt("Hello World", 2)
print("Encrypted :", enc)
dec = fn.decrypt(enc, 2)
print("Decrpyted :", dec)
