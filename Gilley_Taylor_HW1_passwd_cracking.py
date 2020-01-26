# cryptography: making sensitive information unreadable and thus secure
# encryption: transfering file from one computer to another
# hashing: better for hashing (add salt, etc.)

import hashlib, binascii
from itertools import *
# 100000 iteration sha256 hashing of that hash of that hash and so on...
# great hashing with salt method
# dk = hashlib.pbkdf2_hmac('sha256', b'hello', b's', 100000)
# print(binascii.hexlify(dk))

## Create a function that returns a list of possible numbers to hash

# returns a list of all of the cartesian product of !,#,*,~, 0...9
# first digit must be a special character
def five_digit_list():
    # creating cartesian product
    last_four = product('0123456789#!*~', repeat=4)

    # creating cartesian and final list
    cart = []
    count = 0
    final = []

    # creating a list of the cartesian products and adding them to cartesian list
    for it in last_four:
        string = ""
        for element in it:
            string += str(element)

        cart.append(string)

    beg = ['!', '*', '#', '~']

    for i in beg:
        for j in cart:
            final.append(i+j)
            count += 1

    return final











def main():

    crypt = hashlib.sha256()
    crypt.update(b"programming") # b converts it into binary encoding "unicode-object"
    print(crypt.hexdigest()) # converts string to sha256 then to hex form and prints out
    print(crypt.digest_size)
    print(hashlib.algorithms_available)


    infile = open("words.txt", 'r')

    data = infile.read()

    print(data)
    five_digit_list()

main()