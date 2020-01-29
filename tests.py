# TESTS

from Gilley_Taylor_HW1_passwd_cracking import *

file = open("test_in.txt", "w")

# Writes all the test username:password:other's below to the test_in file to read from
# The passwords displayed in test_out.txt should reflect those in the comments below

# RULE 1 ########################################
# Testing words that are seven characters long

# Danny's expected password is Bismark9
print("danny:fe488b10bcd7f16a3efbfb2710bd724e93dc1cc7f61cf49059d8b1b26883d25b:other", file=file)

# Ernie's expected password is Zooming3
print("ernie:dc7681d28545888687f802f93805634255d026c0981278b86f65b0f279f4fe52:other", file=file)

# Patricia's expected password is Yachted0
print("patricia:7ab599aa2a07c43d2317de540b3d1d32513037bde599abf9bd43e1e687fd4308:other", file=file)

# RULE 2 ########################################
# Testing 5 digit password with at least one '~!# or *' at the beginning

# John's expected password is !!00*
print("john:175952f9cf5d6fcdc307643b9ecc95e305693884e659d9c6979cdd7b790b6c92:other", file=file)

# Alice's expected password is *999*
print("alice:4996305f5689d635c98af7b53a663196ddec1e0bd4d4b985aaff0c7a0b1902d7:other", file=file)

# Donnie's expected password is !*#*~
print("donnie:9dd3974cc9fee0652f35f2a7a4481a9c8e7f4b00ea72e86fe6fd7d42e4f8c060:other", file=file)

# RULE 3 ##########################################
# Testing five character word with a letter a -> @ and l -> 1

# Monique's expected password is Afghanistan
print("monique:5dbddf911f9e565299428e948a92ea5d1943c4099db883cc4491cb32cc757de8:other", file=file)

# Patrick's expected password is leadership
print("patrick:9e720e53885580b1e0c5866c98e04988f0b0d071037fb54621a5180ba29e72e7:other", file=file)

# Dave's expected password is leafletting
print("dave:87e1eb2af244cae9dbd8b67a0b49ea8c600944c8c6170710058d20a272878743:other", file=file)

# RULE 4 ##########################################
# Testing word that is made with digits up to 7 digits in length

# Carl's passwords is 99364
print("carl:11df08cc7f9bd4a89e51bb7f3983de4c0a82f222062af37dd960bccef9465f77:other", file=file)

# Paul's password is 4000
print("paul:b090147020e033534635010c4f7eb6fc270d44e5df67ea9e744a8087df9ca106:other", file=file)

# Samantha's password is 4736285
print("samantha:21734eee70713f0a09a313044393af2c6a5e0e71d74f9923c42a2ba4a739f2d7:other", file=file)

# RULE 5 #########################################
# Testing single word of any length

# Al-gorithm's password is A
print("alorithm:559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd:other", file=file)

# Code-y's password is electroencephalogram
print("codey:0d36c2425ba0be53e56b9648754fa056070910cd56ae9299e0dc411ba50299ca:other", file=file)

# Maybell's password is zonked
print("maybell:292670667ec43333bdc9382dbc26c47af1d0ef523e12242cee94ab5c0f85f753:other", file=file)

file.close()

r_w_passwords("test_in.txt", "test_out.txt")