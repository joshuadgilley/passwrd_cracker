# cryptography: making sensitive information unreadable and thus secure
# encryption: transfering file from one computer to another
# hashing: better for hashing (add salt, etc.)

import hashlib, binascii
# 100000 iteration sha256 hashing of that hash of that hash and so on...
# great hashing with salt method
dk = hashlib.pbkdf2_hmac('sha256', b'hello', b's', 100000)
print(binascii.hexlify(dk));

# crypt = hashlib.sha256()
# crypt.update(b"hello") # b converts it into binary encoding "unicode-object"
# print(crypt.hexdigest()) # converts string to sha256 then to hex form and prints out
# print(crypt.digest_size)
# print(hashlib.algorithms_available)
