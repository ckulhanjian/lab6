def main():
    password = input('Enter an 8-digit password: ')
    new_password = ""

    for i in password:
        new_password += int(i)+3

if __name__ == '__main__':
    main()
