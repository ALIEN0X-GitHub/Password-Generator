import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")
    try:
        # Get user input for password length
        length = int(input("Enter the length of the password (6-128): ") or 12)
        if not 6 <= length <= 128:
            raise ValueError("Password length must be between 6 and 128 characters.")
        
        # Get user input for character sets
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
        
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        
        print("\nGenerated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
