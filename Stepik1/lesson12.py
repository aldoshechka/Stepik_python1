a, b, c = int(input()), int(input()), int(input())
if a >= b:
    if a >= c:
        if b >= c:
            print(a, '\n', c, '\n', b)
        else:
            print(a, '\n', b, '\n', c)
    else:
        print(c, '\n', b, '\n', a)
elif b >= c:
    if a >= c:
        print(b, '\n', c, '\n', a)
    else:
        print(b, '\n', a, '\n', c)
else:
    print(c, '\n', a, '\n', b)
