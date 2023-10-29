def main():
    while True:
        print('\nMenu')
        print('--------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        menu_option = int(input('\nPlease enter an option: '))

        if menu_option == 1:
            new_password = encoder()
            print('Your password has been encoded and stored!')
        if menu_option == 2:
            print(f"Your encoded password is {new_password}, and the original password is {'place_holder'}.")
        if menu_option == 3:
            break

def encoder():
    password = input('Enter an 8-digit password: ')
    new_password = ""
    for i in password:
        new_password += str(int(i)+3)

    return new_password

def decoder(password):
    decoded_password = ''
    for i in range(0, len(password)):
        decoded_password += str(int(i) - 3)
    return decoded_password

if __name__ == "__main__":
    main()
