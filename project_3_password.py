# Password Generator

import random

print("Password Generator\n")

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()1234567890?'

number = input ("Enter no. of passwords to generate: ")
number = int(number)

length = input("Enter length of passwords: ")
length = int(length)

print('\n Here are your passwords: \n')
for pwd in range(number):
    passwords = ''
    for i in range(length):
        passwords += random.choice(chars)
    print(passwords)