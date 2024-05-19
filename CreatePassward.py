import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
print("WELLCOME TO PASSWORD GENERATOR")
nr_letters=int(input("How many letters you would like enter to make password"))
nr_symbols=int(input("how many symbols"))
nr_numbers=int(input("How many numbers"))
password=""
for char in range(1, nr_letters+1):
    random_char=random.choice(letters)
    password+=random_char
for char in range(1, nr_symbols+1):
    random_char=random.choice(symbols)
    password+=random_char   
for char in range(1, nr_numbers+1):
    random_char=random.choice(numbers)
    password+=random_char 
print(password)   