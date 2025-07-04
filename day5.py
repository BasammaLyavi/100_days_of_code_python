"""import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z']

numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
           ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']


print("welcome to password creating project\n")
nr_letters=int(input("How many letters you want?\n"))
nr_numbers=int(input("How many numbers you want?\n"))
nr_symbols=int(input("How many symbols you want?\n"))

password=" "
for char in range(0,nr_letters):
    password+=random.choice(letters)

for char in range(0,nr_numbers):
    password+=random.choice(numbers)

for char in range(0,nr_symbols):
    password+=random.choice(symbols)
print(password)"""


import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z']



symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
           ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("welcome to password creating project\n")

nr_letters=int(input("How many letters you want?\n"))
nr_symbols=int(input("How many symbols you want?\n"))
nr_numbers=int(input("How many numbers you want?\n"))
password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

print("password_list")
random.shuffle(password_list)
print("password_list")

password=' '
for char in password_list:
    password+=char
print(f"your password is {password}💀")



