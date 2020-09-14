def highest_even(li):
    maxVal = 0
    for item in li:
        if (item % 2 == 0):
            if item > maxVal:
                maxVal = item
                # print('this is even')
            else:
                continue
        else:
            # print('this is odd')
            continue

    return maxVal


print(highest_even([10, 20, 311, 440, 80, 11]))
