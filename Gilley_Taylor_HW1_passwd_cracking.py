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

import hashlib, types

hexCode = "Maggie:ab2620f9b7154d9f9dc1b3c2d949d85d595fe77f45411b3dbe6e5b47da564177:42:20:MaggieSimpson:/home/maggie:/bin/tcsh"

arr = hexCode.split(":")

password = arr[1]

print(password)


# validation methods for main rules method
def seven_letter_cap(word):
    valid = False

    if len(word) == 7 and word.isalpha:
        valid = True

    return valid


def five_digit_special_begin(num):
    valid = False

    if ('*' in num[:1] or '~' in num[:1] or '!' in num[:1] or '#' in num[:1]) and len(num) == 5:
        valid = True

    return valid

def five_letter_a_l_switch(word):
    valid = False

    if len(word) == 5 and word.isalpha() and ('a' in word and 'l' in word):
        valid = True

    return valid

def up_to_seven_digits(num):
    valid = False

    if len(num) <= 7 and num.isnumeric():
        valid = True

    return valid

def  single_words_no_spaces(word):
    valid = False

    if word.isalpha() and ' ' in word == False:
        valid = True

    return valid


# main rules method
def rules(word):

    if five_digit_special_begin(word):
        return str(word)

    elif five_letter_a_l_switch(word):
        w = list(word)
        i = w.index('a')
        j = w.index('l')
        arr[i] = '@'
        arr[j] = '1'
        "".join(w)
        return str(w)

    elif up_to_seven_digits(word):
        return str(word)
    elif single_words_no_spaces(word):
        return str(word)
    else:
        return ""

# fileIO



def main():
    infile = open("words.txt", "r")

    for line in infile:

        line = line.strip()

        if seven_letter_cap(line):
            word_list = []
            i = 0
            line.capitalize()
            while i < 10:
                word_list.append(line + str(i))
                i += 1
            fin = word_list
        else:
            fin = rules(line)

        if isinstance(fin, list):
            j = 0
            while j < len(fin):
                crypt = hashlib.sha256()
                crypt.update(fin[j].encode('utf-8'))
                new_pass = crypt.hexdigest()
                j += 1
                if password == new_pass:
                    print(fin[j] + "is the password")
        elif fin == "":
            continue
        else:
            crypt = hashlib.sha256()
            crypt.update(fin.encode('utf-8'))
            new_pass = crypt.hexdigest()
            if password == new_pass:
                print(fin + "is the password")


main()

