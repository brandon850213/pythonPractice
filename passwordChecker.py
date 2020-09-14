name = input('Enter your name: ')
password = input('Enter your password carefully: ')
counts = len(password)
hide_password = '*' * counts
print(f'Hi {name}! your password {hide_password} is {counts} letters long.')
