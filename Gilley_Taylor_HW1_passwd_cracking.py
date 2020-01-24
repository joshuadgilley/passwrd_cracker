# cryptography: making sensitive information unreadable and thus secure
# encryption: transfering file from one computer to another
# hashing: better for hashing (add salt, etc.)


# 100000 iteration sha256 hashing of that hash of that hash and so on...
# great hashing with salt method
# dk = hashlib.pbkdf2_hmac('sha256', b'hello', b's', 100000)
# print(binascii.hexlify(dk))

#crypt = hashlib.sha256()
#crypt.update(b"programming") # b converts it into binary encoding "unicode-object"
#print(crypt.hexdigest()) # converts string to sha256 then to hex form and prints out
#print(crypt.digest_size)
#print(hashlib.algorithms_available)


#def length(string):
    #print(len(string))

# length('ab2620f9b7154d9f9dc1b3c2d949d85d595fe77f45411b3dbe6e5b47da564177')
#
#
# length('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')

import hashlib, binascii

hexCode = "Maggie:ab2620f9b7154d9f9dc1b3c2d949d85d595fe77f45411b3dbe6e5b47da564177:42:20:MaggieSimpson:/home/maggie:/bin/tcsh"

list = hexCode.split(":")

password = list[1]

print(password)

# fileIO

infile = open("words.txt", "r")
count = 0

for line in infile:

    line = line.strip()

    crypt = hashlib.sha256()
    crypt.update(line.encode('utf-8'))
    newPass = crypt.hexdigest()

    print(newPass)

    if password == newPass:
        print(line + " is the password...")
        break


def addAsandLs():
    print("hello world")

