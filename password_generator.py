import random
import string

# Use string module for character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

def generate_password(min_length=8):
    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),         # At least one uppercase letter
        random.choice(lowercase),         # At least one lowercase letter
        random.choice(digits),            # At least one number
        random.choice(special_characters) # At least one special character
    ]
    
    # Fill the rest of the password to meet the minimum length
    if len(password) < min_length:
        remaining_length = min_length - len(password)
        all_characters = uppercase + lowercase + digits + special_characters
        password += random.choices(all_characters, k=remaining_length)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

print('Welcome to the Password Generator!')

while True:
    # Generate and print the password
    password = generate_password()
    print(f'Your new password is: {password}')
    
    # Ask if the user wants another password
    response = input('Would you like another password? Type y or n: ').lower()
    if response == 'n':
        break