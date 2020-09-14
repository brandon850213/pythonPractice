def test(a):
    # '''
    # Info: Its for testing
    # '''
    # print(a)
    for item in a:
        if item % 2 == 0:
            print('even num')
        else:
            continue
            print('test')


test([2, 5, 3, 1, 2, 2, 20])
