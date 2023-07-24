password = ""
while password != 'passW1234':
    password = input('Enter a password: ')
print('password is correct!')

if len(password) < 5:
    print('password is weak')
else:
    print('password length is good')

usernames = ["john", "laura", "debbie"]
for i in usernames:
    print(i.capitalize())

username = input("Enter Username: ").lower()
match username:
    case 'john':
        print('Welcome Guest.')
    case 'chris':
        print('Welcome Admin')


