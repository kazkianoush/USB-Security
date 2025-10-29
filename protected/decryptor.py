from cryptography.fernet import Fernet
import os
import sys



if len(sys.argv) < 2:
    print("Usage: python decryptor.py <path>")
    sys.exit(1)


path = sys.argv
path = path[-1]



with open("keyplace.key", 'rb') as f:
    key = f.read()

fernet = Fernet(key)


def decrpt_folder(path):
    for item in os.listdir(path):
        if(item == "protected"):
            continue
        if(os.path.isfile(path+item)):

            with open(path+item, 'rb') as f:
                encrypted = f.read()

                decrypted = fernet.decrypt(encrypted)

            with open(path+item, 'wb') as f:
                f.write(decrypted)

            continue
        elif (os.path.isdir(path+item)):
            decrpt_folder(path+item+'\\')



decrpt_folder(path+'\\')This is a new line
#a
#a
#a
#a
