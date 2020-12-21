x, y = int(input()), int(input())
if y == 0:
    print('Impossible')
    y = int(input('Input non zero value '))
    if y == 0:
        print('User wrong')
    else:
        print(int(x/y))
