my_file = open('test.txt')
print(my_file.read())
my_file.seek(0)  # python read files as cursor, set cursor to 0 to read again
print(my_file.readline())  # only get the first line
print(my_file.readline())  # second one
my_file.seek(0)

print(my_file.readlines())  # read lines return as list

# good way to close the file after using
my_file.close()
