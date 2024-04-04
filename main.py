#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# acumm_letters = ''
password = ''
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
    # x = (random.randint(0, len(letters)))
    # random_letter = letters[x]
    # acumm_letters += random_letter

# acumm_numbers = ''
for number in range(1, nr_numbers + 1):
    password += random.choice(numbers) 
    # y = (random.randint(0, len(numbers)))
    # random_number = str(numbers[y])
    # acumm_numbers += random_number

# acumm_symbols = ''
for symbol in range(1, nr_symbols +1 ):
    password += random.choice(symbols)
    # z = (random.randint(0, len(symbols)))
    # random_symbol = symbols[z]
    # acumm_symbols += random_symbol

print(f'Password order not randomised : {password}')
# print( acumm_letters+acumm_numbers+acumm_symbols)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for symbol in range(1, nr_symbols +1 ):
    password_list.append(random.choice(symbols))

random.shuffle(password_list) #to change the order of the list

new_password = ''
for i in password_list: 
    new_password += i

print(f'Order of characters randomised: {new_password}')
