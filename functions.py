# this is an uncompleted encryption project
# you might find some errors or some problems
# you can find an example in test.py


def encrypt(E_STRING, E_KEY):
    STRLEN = len(E_STRING)

    # entered string vars
    i = -1
    sum = 0

    # used vars
    ENCRYPTED_OUTPUT = []
    STRING_OUTPUT = ""
    LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 127, 144, 132, 134, 136, 138,
     140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160]

    # while loop

    while (i <= STRLEN - 2):
        i += 1
        ENCRYPTED_ASCII = ord(E_STRING[i]) * int(E_KEY)
        ENCRYPTED_STRING = chr(ENCRYPTED_ASCII)
        if (ENCRYPTED_ASCII <= 255):
            if (ENCRYPTED_ASCII in LIST):
                # (MEA-E) means "Multiplying Encryption Algorithm Error"
                # The multiplying encryption algorithm can't encrypt all uppercase chars
                ENCRYPTED_OUTPUT.append("(MEA-E) ")
            else :
                ENCRYPTED_OUTPUT.append(ENCRYPTED_STRING)
        else :
            # debugging
            print("Try to lower your key !")

        if (ENCRYPTED_ASCII == 0):
            # debugging
            print("You can't use zero !")


    # 2nd loop var
    ARRLEN = len(ENCRYPTED_OUTPUT) # array length
    e = -1

    #while loop
    while(e <= ARRLEN - 2):
        e += 1
        STRING_OUTPUT += ENCRYPTED_OUTPUT[e]
        # print(STRING_OUTPUT)

    # returns the encrypted string
    return STRING_OUTPUT


def decrypt(D_STRING, D_KEY):

    # user vars
    s = -1
    DSTRLEN = len(D_STRING)
    DECRYPT_OUTPUT = []

    # while loop
    while (s <= DSTRLEN - 2):
        s += 1
        DECRYPT_OUTPUT.append(ord(D_STRING[s]))

    # 2nd loop vars
    DARRLEN = len(DECRYPT_OUTPUT)
    DECRYPTED_ASCII = 0
    DTOASCII = 0
    DECRYPTED_ARRAY = []
    DSTRING_OUTPUT = ""

    t = -1

    while (t <= DARRLEN - 2):
        t += 1
        DECRYPTED_ASCII = int(DECRYPT_OUTPUT[t] / int(D_KEY))
        DTOASCII = chr(DECRYPTED_ASCII)
        DECRYPTED_ARRAY.append(DTOASCII)
        DSTRING_OUTPUT += DECRYPTED_ARRAY[t]

    return DSTRING_OUTPUT
