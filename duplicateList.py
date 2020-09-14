# Exercise : check for duplicates in list

# Solution 1
# duplicate_list = []

# for i in set(some_list):
#   if some_list.count(i) > 1:
#     duplicate_list.append(i)
# print(duplicate_list)

some_list = ['a', 'b', 'c', 'a', 'd', 'c', 'b', 'm', 'n']
check_list = []
duplicate_list = []

for i in some_list:
    if i in check_list:
        duplicate_list.append(i)
    else:
        check_list.append(i)

print(f'this is check_list {check_list}')
print(f'the duplicate part is {duplicate_list}')
