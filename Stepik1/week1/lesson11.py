pi = 3.14
d = input()
if d == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif d == 'прямоугольник':
    a, b = int(input()), int(input())
    s = a * b
elif d == 'круг':
    r = int(input())
    s = pi * r**2
else:
    print('Unknown figure')
print(float(s))
