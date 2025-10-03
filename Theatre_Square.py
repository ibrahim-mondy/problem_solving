n,m,a = map(int, input().split())

x = (n + a - 1) // a
y = (m + a - 1) // a

print(x * y)
# another way

# import math

# n, m, a = map(int, input().split())

# x = math.ceil(n/a)
# y = math.ceil(m/a)
# print(x * y)