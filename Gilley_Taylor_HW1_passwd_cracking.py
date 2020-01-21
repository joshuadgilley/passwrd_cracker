# cryptography: making sensitive information unreadable and thus secure
# encryption: transfering file from one computer to another
# hashing: better for hashing (add salt, etc.)

import hashlib

crypt = hashlib.sha256()
crypt.update(b"hello") # b converts it into binary encoding "unicode-object"
print(crypt.hexdigest()) # converts string to sha256 then to hex form and prints out
print(crypt.digest_size)

