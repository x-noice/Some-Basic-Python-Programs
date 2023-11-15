list_1=[]
size = int(input('Enter list size: '))
for i in range(size):
    el=int(input('Enter element: '))
    list_1.append(el)
list_1.insert(0,list_1.pop())
print(list_1)