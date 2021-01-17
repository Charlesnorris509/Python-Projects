"""This is the code for a secure password generator 
using python3.9.1 by @CharlesNorris the 17/01/2021
using digits , symbols, words and a length of 18 characters"""

import random
from string import digits, punctuation, ascii_letters

password_length = 18
secure_password_generator = random.SystemRandom()
password = "".join(secure_password_generator.choice(symbols))
for i in range(password_length):
    print(password)

