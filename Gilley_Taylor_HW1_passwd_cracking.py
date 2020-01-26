#################################################
# Josh Gilley and Chris Taylor                ###
# College of Charleston CS / Network Security ###
# January 30, 2020                            ###
#################################################

# import hashing and graphics library
import hashlib
from graphics import *


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


# MAIN RULES METHOD (USING VALIDATION METHODS)
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


def main():
    # GUI
    # Set window
    win = GraphWin("Pass Kraken", 1000, 800)
    win.setBackground("teal")

    # Set title, entry bar, submit
    message = Text(Point(500,200), "Pass Kraken")
    message.setTextColor("lightcyan")
    message.setFace("courier")
    message.setSize(36)
    message.setStyle("bold italic")
    inputbox = Entry(Point(500,300), 70)
    inputbox.setTextColor("lightcyan")
    submit = Text(Point(700, 330), "Submit")
    submit.setTextColor("lightcyan")
    submit.setFace("courier")
    submit.setSize(18)

    # kraken img credit: Artist: CHENXIN Website: pngtree.com
    kraken = Image(Point(470, 480), "newoc.png")

    # draw kraken, submit, message, entry box
    kraken.draw(win)
    submit.draw(win)
    inputbox.draw(win)
    message.draw(win)

    # after retrieving entry, display results and exit
    result = Text(Point(500, 600), "Unable to Crack")
    result.setSize(36)
    result.setFill("teal")
    result.setOutline("dimgrey)")
    result.setTextColor("white")
    result.setFace("courier")

    result2 = Text(Point(500, 600), "Unable to Crack")
    result2.setSize(36)
    result2.setFill("teal")
    result2.setOutline("dimgrey)")
    result2.setTextColor("white")
    result2.setFace("courier")

    exit = Text(Point(500, 640), "Exit")
    exit.setSize(20)
    exit.setTextColor("lightcyan")
    exit.setFace("courier")
    exit.setStyle("italic")

    # get a click to close
    win.getMouse()

    # password from entry bar
    password_split = inputbox.getText().split(":")
    password = password_split[1]

    # open .txt file
    infile = open("words.txt", "r")

    cracked = False

    # cycle through each word in file
    for line in infile:

        # clean word of any added additional (/n /t etc..)
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
                    # post cracked password
                    cracked = True
                    result.setText(fin[j] + " is your cracked password!")
                    result.draw(win)
                    exit.draw(win)
                    win.getMouse()
                    win.close()
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
                cracked = True

                # post cracked password
                result2.setText(fin + " is your cracked password!")
                result2.draw(win)
                exit.draw(win)
                win.getMouse()
                win.close()
                break

    # if the password is not matched, output message saying so
    if not cracked:
        # post failed password retrieval in GUI
        result.setText("Unable to find Password..")
        result.draw(win)
        exit.draw(win)
        win.getMouse()
        win.close()


main()

