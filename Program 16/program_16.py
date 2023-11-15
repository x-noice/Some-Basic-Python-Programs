list_1=[]
eve_smallest = 0
eve_largest = 0
eve_count = 0
listLen = int(input('Enter the size of the list: '))
for i in range(listLen):
    el = eval(input('Enter the element: '))
    if(el%2==0):
        eve_count+=1
    list_1.append(el)
list_1.sort()

if(eve_count==0):
    print('No even element.')
else:
    while eve_smallest==0:
        for j in list_1:
            if(j%2==0 and eve_smallest == 0):
                eve_smallest=j
    while eve_largest==0:
        for j in list_1:
            if(j%2==0):
                eve_largest=j
    print('Smallest even no. =',eve_smallest)
    print('Largest even no. =',eve_largest)