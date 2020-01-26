#################################################
# Josh Gilley and Chris Taylor                ###
# College of Charleston CS / Network Security ###
# January 30, 2020                            ###
#################################################

# import hashing and graphics library
import hashlib

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


def main():

    # open .txt file
    infile = open("words.txt", "r")

    password_split = input("Please enter the username:password:other::::").split(":")
    password = password_split[1]

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
            j = 0
            while j < len(fin):
                crypt = hashlib.sha256()
                crypt.update(fin[j].encode('utf-8'))
                new_pass = crypt.hexdigest()
                j += 1
                if password == new_pass:
                    # post cracked password
                    print(fin[j] + " is the password")
                    break

        # if word doesn't fit rules, skip it
        elif fin == "":
            continue

        # if fin is a tuple/string the hash it and compare!
        elif not(isinstance(fin, list)):
            crypt = hashlib.sha256()
            crypt.update(fin.encode('utf-8'))
            new_pass = crypt.hexdigest()
            if password == new_pass:
                print(fin + " is the password")
                break

    # here we have broken out of the dictionary meaning that we need to check rule #2 and #4



main()

