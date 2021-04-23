# TESTS

from Gilley_Taylor_HW1_passwd_cracking import *

file = open("test_in.txt", "w")

# Writes all the test username:password:other's below to the test_in file to read from
# The passwords displayed in test_out.txt should reflect those in the comments below



###########RULE 1 ########################################")
###########Testing words that are seven characters long###########")

# Danny's expected password is Bismite9
print("danny:937cbebf533bdb4b2b671286fdfedb8244d19b9b82ddb6f72a7206586dd3b965:other", file=file)

# Ernie's expected password is Zyzomys3
print("ernie:4b2c1449f2c0c942c056cb681fcfd15e7702de9f66204c6fb16b91d29665b6c9:other", file=file)

# Patricia's expected password is Wiggish0
print("patricia:814d8d163812b67a57f7cf8a9212c3016b7e5c11716a6bfff005ef620af6e40e:other", file=file)



########### RULE 2 ########################################")
###########Testing 5 digit password with at least one '~!# or *' at the beginning###########")

# John's expected password is !!00*
print("john:175952f9cf5d6fcdc307643b9ecc95e305693884e659d9c6979cdd7b790b6c92:other", file=file)

# Alice's expected password is *999*
print("alice:4996305f5689d635c98af7b53a663196ddec1e0bd4d4b985aaff0c7a0b1902d7:other", file=file)

# Donnie's expected password is !*#*~
print("donnie:9dd3974cc9fee0652f35f2a7a4481a9c8e7f4b00ea72e86fe6fd7d42e4f8c060:other", file=file)



########### RULE 3 ##########################################
###########Testing five character word with a letter a -> @ and l -> 1###########")

# Monique's expected password is 1inj@
print("monique:b31e111610cd7da64f39da9f4ab8afbd145324ecb6c751e145642b50d641690d:other", file=file)

# Patrick's expected password is @gi1e
print("patrick:281841ae8d2eb422016a04f4d472c6e3c4b90bf8a995e94d6ee66b95a23dc1a3:other", file=file)

# Dave's expected password is 11@m@
print("dave:035d931c3c8c00b20f1dc74d2e5dc2fcc677ab2e65e19eba887dece1c63fee82:other", file=file)

# Trey's expected password is be@ch
print("dave:e77599c90db264dbe4b449565a03b5a26c989e975089fcc7dc3c55a720928e66:other", file=file)

# Prin's expected password is co1in
print("dave:69a1ef7779e95650e82664ecbe65a935778a302ad67d00169d8cf1d3c7885587:other", file=file)



########### RULE 4 ##########################################")
########### Testing word that is made with digits up to 7 digits in length")

# Carl's passwords is 99364
print("carl:11df08cc7f9bd4a89e51bb7f3983de4c0a82f222062af37dd960bccef9465f77:other", file=file)

# Paul's password is 400000
print("paul:ad1e2e29fe1631ddf7bedaadffe63c4efd61e6909a1ed0648e7b9645bd27dab5:other", file=file)

# Samantha's password is 4736285
print("samantha:21734eee70713f0a09a313044393af2c6a5e0e71d74f9923c42a2ba4a739f2d7:other", file=file)



########### RULE 5 #########################################")
########### Testing single word of any length###########")

# Al-gorithm's password is A
print("alorithm:559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd:other", file=file)

# Code-y's password is electroencephalogram
print("codey:0d36c2425ba0be53e56b9648754fa056070910cd56ae9299e0dc411ba50299ca:other", file=file)

# TESTING A NOT FOUND PASSWORD ##################################################

# Should fail's password is not**gonnaWrk
print("shouldFail:b5ac06f81a0aa5ef9d60efb73eb7efe13607f3b683d4eda02698886bc6e82cd2:other", file=file)

file.close()

r_w_passwords("test_in.txt", "test_out.txt")