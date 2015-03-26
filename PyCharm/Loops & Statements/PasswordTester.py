print('Welcome to password tester')

password = input('Enter your password: ')
if password == 'school':
    print('Access granted')
    input('\n\nPress enter key to exit')
else:
    print('Access denied!')
    


print('---------------------------------------------')

password = input('2nd chance, enter your password: ')
if password == 'school':
    print('Access granted')
else:
    print('Access denied, 1 more chance!')

print('---------------------------------------------')

password = input('Last chance, enter your password: ')
if password == 'school':
    print('Access granted')
else:
    print('Access denied!')

    
#When indent occurs, an indent is created
    
input('\n\nPress enter key to exit')

#Input is what's entered after (enter your password), puts into password var
#If password = school prints line below
#'else' being if-false (boolean) and prints said text
