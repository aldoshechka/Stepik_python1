x = int(input())
x1 = x // 1000
x2 = x % 1000
sum1 = x1 // 100 + (x1 % 100) // 10 + (x1 % 100) % 10
sum2 = x2 // 100 + (x2 % 100) // 10 + (x2 % 100) % 10
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')
