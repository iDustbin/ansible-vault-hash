from passlib.hash import sha512_crypt
password = input('Enter String to hash: ')
hash = sha512_crypt.hash(password)
print(hash)
