# TESTS
from Gilley_Taylor_HW1_passwd_cracking import main as main_test

# RULES
# 1.) 7 letter word
# 2.) 5 digit number with 'at least one' *, !, #, ~ in beginning
# 3.) 5 letter word with a OR l
# 4.) 1-7 digit number from 0 to 9999999
# 5.) any single word



# TESTING FOR RULE 1
rule1 = ["homer:84b175349a3d5a8bcabda1ab8eb84e3c36139f27e3a04b17b47c497a3b577940:20:Homer Simpson:/home/homer:/bin/tcsh"]

# TESTING FOR RULE 2
rule2 = ["lisa:e77599c90db264dbe4b449565a03b5a26c989e975089fcc7dc3c55a720928e66:353:Lisa Simpson:/home/lisa:/bin/tcsh"]

# TESTING FOR RULE 3
rule3 = ["lisa:e77599c90db264dbe4b449565a03b5a26c989e975089fcc7dc3c55a720928e66:353:Lisa Simpson:/home/lisa:/bin/tcsh"]

# TESTING FOR RULE 4
rule4 = ["lisa:e77599c90db264dbe4b449565a03b5a26c989e975089fcc7dc3c55a720928e66:353:Lisa Simpson:/home/lisa:/bin/tcsh"]

# TESTING FOR RULE 5
rule5 = ["Maggie:ab2620f9b7154d9f9dc1b3c2d949d85d595fe77f45411b3dbe6e5b47da564177:42:20:Maggie Simpson:/home/maggie:/bin/tcsh"]

# TESTING FOR UNACCEPTED STRINGS AND SPECIAL CASES
rule6 = ["marge:3564c21155d772de5cb58ba122d2131f1c060bdf081730ea9518a45bd966c2e4:351:Marge Simpson:/home/marge:/bin/tcsh"]

expected_output = ["Puzzles4 -> \r"]

rules = [rule1, rule2, rule3, rule4, rule5, rule6]


# iterates through every test path...
def test():
    for rule in rules:
        for path in rule:
            main_test(path)




