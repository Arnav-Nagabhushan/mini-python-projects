import random
import string

def get_password_length():
    while True:
        length = input('Enter desired password length: ')

        try:
            length = int(length)
            
            if length > 0:
                return length
            
            else:
                print('Please enter a valid password length!')

        except ValueError:
            print('Please enter a valid password length!')

def generate_password(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = ''
    
    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print('Welcome to Password Generator!')
    
    length = get_password_length()
    password = generate_password(length)

    print('\nYour password has been generated successfully!')
    print(f'Your password is: \t{password}')

if __name__ == "__main__":
    main()
