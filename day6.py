import random
import string

length = int (input("Password length:"))
chars = string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(length):
   password = password + random.choice(chars)

print("Your password is:",password)