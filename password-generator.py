'''
Name: Charlie Man
Date: 1/28/24
password-generator.py

Description: This is the main program file to run the random password
generator.
'''

import random

# function to shuffle all characters of string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

# main program
uppercase_letter_1 = chr(random.randint(65,90))
uppercase_letter_2 = chr(random.randint(65,90))

lowercase_letter_1 = chr(random.randint(97,122))
lowercase_letter_2 = chr(random.randint(97,122))

digit_1 = str(random.randint(0,9))
digit_2 = str(random.randint(0,9))

punctuation_list = [random.randint(33,47), random.randint(58,64),
                    random.randint(91,96), random.randint(123,126)]
punctuation_sign_1 = chr(random.choice(punctuation_list))
punctuation_sign_2 = chr(random.choice(punctuation_list))

# generate password using all characters in random order
password = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + \
           lowercase_letter_2 + digit_1 + digit_2 + punctuation_sign_1 + \
           punctuation_sign_2
password = shuffle(password)

# output
print(password)
