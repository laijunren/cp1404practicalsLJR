names = {}
while True:
    email = input('Email: ')
    if email == '':
        break
    name = ' '.join(email.split('@', 1)[0].split('.')).title()
    flag = input('Is your name ' + name + '? (Y/n) ').upper()
    if flag == 'N' or flag.upper() == 'NO':
        name = input('Name: ')
    names[email] = name.title()
for email, name in names.items():
    print(name + ' (' + email + ')')
