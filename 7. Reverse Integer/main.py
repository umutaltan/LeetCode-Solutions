x = 1234
sign = 1
if x < 0:
    x = -x
    sign = -1
y = 0
length = len(str(x))
for i in range(1,length+1):
    y += (x % 10) * (10 ** (length - i))
    x //= 10

if sign == -1:
    y = -y
if not -2**31 <= y <= 2**31 - 1:
    print(0)
print(y)