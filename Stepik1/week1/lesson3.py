x = int(input())
h = int(input())
m = int(input())
summary = x + h * 60 + m
print(summary // 60, summary % 60)