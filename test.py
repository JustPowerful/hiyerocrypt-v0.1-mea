# importing the script
import functions as fn

# using the function
enc = fn.encrypt("Hello World")
print("Encrypted :", enc)
dec = fn.decrypt(enc)
print("Decrpyted :", dec)
