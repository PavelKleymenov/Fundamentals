"""Implement a program that generates a random password using a specific set of characters"""
import secrets, string

"""Build a set of characters that may be used in a password"""
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Store the set in a corresponding variable
alphabet = letters + digits + special_chars

# Determine how long a password should be
pwd_length = 12

# Generate a password
pwd = ''
for _ in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

# Print out the password
print(pwd)
