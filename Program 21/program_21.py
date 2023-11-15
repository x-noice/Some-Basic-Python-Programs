size = int(input('Enter no. of values: '))
tup1 = ()
for i in range(size):
    el = eval(input('Enter an element: '))
    tup1 = tup1 + (el,)
for i in tup1:
    print(i)
print('Maximum value:',max(tup1))
print('Minimum value:',min(tup1))