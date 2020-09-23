import re
# password checker:
# 1. 8 character long
# 2.contain any sort letters,nums,$%#@
pattern = re.compile(r'^[\da-zA-z#$%@]{8,}')
while True:
    string = input('Enter your password:')
    a = pattern.fullmatch(string)
    if a:
        print('Your password is valid')
        break
    else:
        print('Please enter again')
