n = int(input('Enter a no: '))
f = -1
s = 1
for i in range(n):
    t = f + s
    print(t, end = '\t')
    f = s
    s = t
