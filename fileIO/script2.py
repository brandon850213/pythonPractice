# with open('test.txt') as my_file:
#     print(my_file.readlines())

with open('smile.txt', mode = 'a') as my_file:
    text = my_file.write("\nToday is a happy day.")
    print(text)