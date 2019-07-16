# YOU MIGHT FIND SOME ERRORS AND BUGS IN THIS PROGRAM
# YOU CAN REPORT IT USING THE ISSUES REPORT IN GITHUB
# YOU CAN FIND AN EXAMPLE ON HOW TO USE THE SCRIPT ON test.py

LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
APPL = ["Д", "Ь", "ξ", "Δ", "Э", "Ч", "Б", "Ц", "φ", "Г", "χ", "π", "ψ" ,"ω" ,"Ю", "Ω"]

def encrypt(E_STRING):
    STRLEN = len(E_STRING)

    # entered string vars
    i = -1
    sum = 0

    # used vars
    ENCRYPTED_OUTPUT = []
    STRING_OUTPUT = ""

    # while loop

    while (i <= STRLEN - 2):
        i += 1
        ENCRYPTED_ASCII = ord(E_STRING[i]) * 2
        ENCRYPTED_STRING = chr(ENCRYPTED_ASCII)
        if (ENCRYPTED_ASCII <= 255):
            if (E_STRING[i] in LIST):
                INDEX = LIST.index(E_STRING[i])
                ENCRYPTED_OUTPUT.append(APPL[INDEX])

                # # (MEA-E) means "Multiplying Encryption Algorithm Error"
                # # The multiplying encryption algorithm can't encrypt all uppercase chars
                # ENCRYPTED_OUTPUT.append("(MEA-E) ")
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


def decrypt(D_STRING):

    n = -1
    DLEN = len(D_STRING) - 2

    DECRYPTED_OUTPUT = []

    while (n <= DLEN):
        n += 1
        if (D_STRING[n] in APPL):
            DINDEX = APPL.index(D_STRING[n])
            DECRYPTED_OUTPUT.append(LIST[DINDEX])
        else :
            DINT = int(ord(D_STRING[n]) / 2)
            DCHAR = chr(DINT)
            DECRYPTED_OUTPUT.append(DCHAR)

    k = -1
    DFINALLEN = len(DECRYPTED_OUTPUT) - 2
    OUT_STRING = ""

    while (k <= DFINALLEN):
        k += 1
        OUT_STRING += DECRYPTED_OUTPUT[k]

    return OUT_STRING
