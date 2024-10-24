#Using this code, you will be able to generate strong and random passwords.

import random

print('Write how many characters your password will consist of.')

try:
    s = int(input())
    total = ''

    for i in range(s):
        random_number = random.randint(33, 126) 
        total += chr(random_number)
    
    print('Your password:', total, sep='\n')
    
except ValueError:
    print("Error: Invalid value entered. Please enter an integer.")
