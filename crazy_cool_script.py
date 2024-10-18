import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 16  # You can change this to any desired length
    print(f"Your crazy cool password is: {generate_password(password_length)}")
