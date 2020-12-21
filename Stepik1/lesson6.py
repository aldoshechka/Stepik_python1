a, b, c = int(input()), int(input()), int(input())
if c < a:
    print('Недосып')
elif c > b:
    print('Пересып')
elif a <= c <= b:
    print('Это нормально')
