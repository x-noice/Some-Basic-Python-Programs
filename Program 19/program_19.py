list_1=[]
size = int(input('Enter the no. of elements: '))
for i in range(size):
    el = eval(input('Enter the element: '))
    list_1.append(el)
for i in range(size-1):
    for j in range(size-i-1):
        if(list_1[j]<0):
            list_1[j],list_1[j+1] = list_1[j+1],list_1[j]
print(list_1)