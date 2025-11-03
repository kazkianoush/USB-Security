from cryptography.fernet import Fernet
import os
import sys
import base64



if len(sys.argv) < 2:
    print("Usage: python decryptor.py <path>")
    sys.exit(1)


path = sys.argv
path = path[-1]



with open("keyplace.key", 'rb') as f:
    key = f.read()
    print("Key length:", len(key))
    print("Key looks like:", key)

try:
    fernet = Fernet(key)
    print("Key is valid")
except Exception as e:
    print("Invalid key:", e)


def decrpt_folder(path):
    for item in os.listdir(path):
        print(item)
        # if(item == "protected"):
        #     continue
        if(os.path.isfile(path+item)):
            print("path is file " + path + item)
            with open(path+item, 'rb') as f:
                encrypted = f.read()
                b64 = base64.urlsafe_b64encode(encrypted).decode("ascii")
                print("opened and read raw: " + str(encrypted)[0:10])
                print("opened and read: " + str(b64)[0:10])

                decrypted = fernet.decrypt(encrypted)

            with open(path+item, 'wb') as f:
                f.write(decrypted)

            continue
        elif (os.path.isdir(path+item)):
            decrpt_folder(path+item+'\\')



decrpt_folder(str(path))
