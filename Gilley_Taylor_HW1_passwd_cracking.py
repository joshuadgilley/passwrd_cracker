#################################################
# Josh Gilley and Chris Taylor                ###
# College of Charleston CS / Network Security ###
# January 30, 2020                            ###
#################################################

# import hashing and graphics library
import hashlib
from itertools import product

# crypt function
def cryptic(word_or_num):
    crypt = hashlib.sha256()
    crypt.update(word_or_num.encode('utf-8'))
    encrypted = crypt.hexdigest()
    return encrypted

# VALIDATION METHODS
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

    if len(word) == 5 and word.isalpha() and (word.find('a') != -1 or word.find('l') != -1):
        valid = True

    return valid


def up_to_seven_digits(num):
    valid = False

    if len(num) <= 7 and num.isnumeric():
        valid = True

    return valid


def  single_words_no_spaces(word):
    valid = False

    if word.isalpha() and word.find(" ") == -1:
        valid = True

    return valid


# seven_letter_cap_func that returns the list
def seven_letter_cap_func(word):
    word_list = []
    i = 0
    while i < 10:
        word_list.append(word.capitalize() + str(i))
        i += 1
    return word_list


# MAIN RULES METHOD (USING VALIDATION METHODS)
def rules(word):
    # A five char word with the letter 'a' in it which gets replaced with the special
    # character @ and the character ‘l’ is substituted by the number ‘1’.
    if five_letter_a_l_switch(word):
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

    # Any number of chars single word from /usr/share/dict/words (Linux or Mac)
    elif single_words_no_spaces(word):
        return str(word)

    # If dictionary word doesn't match rules, return empty string
    else:
        return ""


# Rule #4 any word that is made with digits up to 7 digits length.
def up_to_seven_digits():
    count = 0
    i = 7
    cart = []

    while(i > 0):
        prod = product('0123456789', repeat=i)

        for it in prod:
            string = ""
            count += 1
            for element in it:
                string += str(element)
            cart.append(string)
        i -= 1

    return cart

def cart_helper(cart, password):

    for it in cart:
        if password == cryptic(it):
            return it


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



def r_w_passwords(userIn, userOut):

    if userIn == "no_args" and userOut == "no_args":
        userfile = input("Please enter the .txt file with 'username:password:other' on each line: ")
        user_out = input("Please enter the .txt file you would like to write to:")

    else:
        userfile = userIn
        user_out = userOut

    print()
    infile = open(userfile, "r")
    outfile = open(user_out, "w")

    for line in infile:
        username = line.split(":")[0]
        print("Trying to crack " + username + "'s password... ")
        cracked = main(line)
        if cracked is not None:

            print("Success!")
            print("Password is: " + cracked)
            print(cracked, file=outfile)
            print("Wrote to " + user_out)
            print()
            print("-------------------------------------")
            print()

        else:
            print("Unsuccessful :^(")
            print(username + "'s password couldn't be found...", file=outfile)
            print("Wrote to " + user_out)
            print()
            print("-------------------------------------")
            print()



def main(file_line):

    # open .txt file
    infile = open("words.txt", "r")

    password = file_line.split(":")[1].strip()

    # cycle through each word in file
    for line in infile:

        # clean word of any added additional (/n /t etc..)
        line = line.strip()

        # seven char word which gets the first letter capitalized and a 1-digit number appended.
        # if word qualifies, this creates a list of words with the ^ specifications
        if seven_letter_cap(line):
            fin = seven_letter_cap_func(line)

        # if word is not seven_letter_cap list this fin = tuple, word, int, etc.
        else:
            fin = rules(line)

        # if fin is a List, create hashes for every element and compare
        if isinstance(fin, list):

            for it in fin:
                new_pass = cryptic(it)
                if password == new_pass:
                    # post cracked password
                    return it

        # if word doesn't fit rules, skip it
        elif fin == "":
            continue

        # if fin is a tuple/string the hash it and compare!
        elif not(isinstance(fin, list)):
            new_pass = cryptic(fin)
            if password == new_pass:
                return fin


    # Here we have broken out of the dictionary meaning that we need to check rule #2 and #4
    five_digit_product = five_digit_list()
    for it in five_digit_product:
        if password == cryptic(it):
            print(it)
            return it

    cartesian_product = up_to_seven_digits()
    for it in cartesian_product:
        if password == cryptic(it):
            print(it)
            return it

    return None


if __name__ == '__main__':
    r_w_passwords("no_args", "no_args")

