x1 = float(input())
x2 = float(input())
y = input()
if x2 == 0 and (y == 'mod' or y == 'div' or y == '/'):
    print('Деление на 0!')
elif y == '+':
    print(x1 + x2)
elif y == '-':
    print(x1 - x2)
elif y == '/':
    print(x1 / x2)
elif y == '*':
    print(x1 * x2)
elif y == 'mod':
    print(x1 % x2)
elif y == 'pow':
    print(x1 ** x2)
elif y == 'div':
    print(x1 // x2)
