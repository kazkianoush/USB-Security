from cryptography.fernet import Fernet
import os
import sys


if len(sys.argv) < 2:
    print("Usage: python encryptor.py <path>")
    sys.exit(1)


path = sys.argv
path = path[-1]


with open("keyplace.key", 'rb') as f:
    key = f.read()

fernet = Fernet(key)



def encrypt_folder(path):
    for item in os.listdir(path):

        print(path+item)
        if(os.path.isfile(path+item)):

            with open(path+item, 'rb') as f:
                original = f.read()

            encrypted = fernet.encrypt(original)

            with open(path+item, 'wb') as f:
                f.write(encrypted)

            ##nussin
            continue
        elif (os.path.isdir(path+item)):
            encrypt_folder(path+item+'\\')
        
        
            

encrypt_folder(str(path)+'\\')
