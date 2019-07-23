# IMPORT THE MODULE
import mea

# IMPORT THE CLASS
api = mea.MEA()

# USE THE MODLUE LIKE THIS
ENCRYPTED = api.encrypt("Hello World")
DECRYPTED = api.decrypt(ENCRYPTED)

# PRINT THE RESULTS
print(ENCRYPTED)
print(DECRYPTED)
