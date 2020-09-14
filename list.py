# What is the output of this code?
# Before you click RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])  # b
print(new_list[-2])  # b
print(new_list[1:3])  # b,c
new_list[0] = 'z'
print(new_list)  # zbc

my_list = [1, 2, 3]
# This will create a new list, therefore line 14 would be 1235 not z235
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)  # z23
print(bonus)  # 1235
