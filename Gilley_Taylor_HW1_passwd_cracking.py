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

import hashlib
from graphics import *


# validation method
def seven_letter_cap(word):
    valid = False

    if len(word) == 7 and word.isalpha:
        valid = True

    return valid

# validation method
def five_digit_special_begin(num):
    valid = False

    if ('*' in num[:1] or '~' in num[:1] or '!' in num[:1] or '#' in num[:1]) and len(num) == 5:
        valid = True

    return valid

# validation method
def five_letter_a_l_switch(word):
    valid = False

    if len(word) == 5 and word.isalpha() and (word.find('a') != -1 or word.find('l') != -1):
        valid = True

    return valid

# validation method
def up_to_seven_digits(num):
    valid = False

    if len(num) <= 7 and num.isnumeric():
        valid = True

    return valid

# validation method
def  single_words_no_spaces(word):
    valid = False

    if word.isalpha() and word.find(" ") == -1:
        valid = True

    return valid


# main rules method
def rules(word):

    # A five digit password with at least one of the following special characters
    # in the beginning: *, ~, !, #
    if five_digit_special_begin(word):
        return str(word)

    # A five char word with the letter 'a' in it which gets replaced with the special
    # character @ and the character ‘l’ is substituted by the number ‘1’.
    elif five_letter_a_l_switch(word):
        w = list(word)

        if word.find('a') != -1 and word.find('l') != -1:
            i = w.index('a')
            j = w.index('l')
            w[i] = '@'
            w[j] = '1'
            b = ''.join(w)
        elif word.find('a') != -1:
            i = w.index('a')
            w[i] = '@'
            b = ''.join(w)
        else:
            i = w.index('l')
            w[i] = '1'
            b = ''.join(w)
        return b

    # Any word that is made with digits up to 7 digits length.
    elif up_to_seven_digits(word):
        return str(word)

    # Any number of chars single word from /usr/share/dict/words (Linux or Mac)
    elif single_words_no_spaces(word):
        return str(word)

    # If dictionary word doesn't match rules, return empty string
    else:
        return ""

# fileIO





def main():
    # GUI
    win = GraphWin("Josh & Chris Password Cracking Tool", 1000, 1000)
    win.setBackground("palevioletred")
    message = Text(Point(500,200), "Pass Kraken")
    message.setTextColor("black")
    message.setFace("courier")
    message.setSize(36)
    message.setStyle("bold italic")
    inputbox = Entry(Point(500,300), 70)
    inputbox.setTextColor("black")
    subText = Text(Point(500, 350), "Submit")
    subText.setTextColor("black")
    subText.setFace("courier")
    subText.setSize(18)
    subText.draw(win)

    result = Text(Point(500, 600), "Unable to Crack")
    result.setSize(36)
    result.setFace("courier")

    exit = Text(Point(500, 640), "Exit")
    exit.setSize(18)
    exit.setFace("courier")
    exit.setStyle("italic")


    inputbox.draw(win)
    message.draw(win)
    win.getMouse()


    password_split = inputbox.getText().split(":")
    password = password_split[1]



    # open .txt file
    infile = open("words.txt", "r")

    # cycle through each word in file
    for line in infile:

        #clean word of any added additional (/n /t etc..)
        line = line.strip()

        # seven char word which gets the first letter capitalized and a 1-digit number appended.
        # if word qualifies, this creates a list of words with the ^ specifications
        if seven_letter_cap(line):
            word_list = []
            i = 0
            while i < 10:
                word_list.append(line.capitalize() + str(i))
                i += 1
            fin = word_list
        # if word is not seven_letter_cap list this fin = tuple, word, int, etc.
        else:
            fin = rules(line)

        # if fin is a List, create hashes for every element and compare
        if isinstance(fin, list):
            j = 0
            while j < len(fin):
                crypt = hashlib.sha256()
                crypt.update(fin[j].encode('utf-8'))
                new_pass = crypt.hexdigest()
                j += 1
                if password == new_pass:
                    result.setText(fin[j] + " is your cracked password!")
                    result.draw(win)
                    exit.draw(win)
                    win.getMouse()
                    break

        # if word doesn't fit rules, skip it
        elif fin == "":
            continue

        # if fin is a tuple/string the hash it and compare!
        else:
            crypt = hashlib.sha256()
            crypt.update(fin.encode('utf-8'))
            new_pass = crypt.hexdigest()
            if password == new_pass:
                result.setText(fin + " is your cracked password!")
                result.draw(win)
                exit.draw(win)
                win.getMouse()




main()

