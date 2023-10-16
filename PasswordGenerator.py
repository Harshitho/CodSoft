import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 4:
        return "Password length should be at least 4 characters."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

try:
    password_length = int(input("Enter the desired length of the password: "))
    generated_password = generate_password(password_length)
    
    print("Generated Password:", generated_password)
except ValueError:
    print("Invalid input. Please enter a valid password length (an integer).")
