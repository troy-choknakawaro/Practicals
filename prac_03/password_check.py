MINIMUM_LENGTH = 2
MAXIMUM_LENGTH = 6

def main():
    password = input("Enter a valid password: ")
    if len(password) < MINIMUM_LENGTH or len(password) > MAXIMUM_LENGTH:
        print("password must be at least {} characters and not more than {} characters".format(MINIMUM_LENGTH,MAXIMUM_LENGTH))
        password = input("Enter a valid password: ")
    else:
        pass

    print('*' * len(password))

main()
