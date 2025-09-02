'''
For this challenge, we will use a Python script to generate a random password of 8 characters. Each time the program is run, a new password will be generated randomly. The passwords generated will be 8 characters long and will have to include the following characters in any order:

2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # etc.
'''

import random

#Selecionando duas letras maiúsculas para a senha 
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))

#Selecionando duas letras minusculas para a senha 

lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))

#Selecionando digitos

number1=chr(random.randint(48,57))
number2=chr(random.randint(48,57))

#Selecionando pontuação.
punctuationSign1=chr(random.randint(32,152))
punctuationSign2=chr(random.randint(32,152))

password= [uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number1 + number2 + punctuationSign1 + punctuationSign2]

random.shuffle(password)
print(f"Sua senha é {password}")