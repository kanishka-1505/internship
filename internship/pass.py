import random

print("Welcome to Password Generator!")

# Ask the user how long the password should be
length = int(input("Enter password length: "))

# Some characters to use in the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*"

# Combine all characters
all_characters = letters + numbers + symbols

# Create password
password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Your password is:", password)