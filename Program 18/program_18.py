a=[]
n = int(input('Enter list size: '))
for i in range(n):
    el=int(input('Enter element: '))
    a.append(el)
ele_search=eval(input("Enter Element you want to search: "))
if ele_search in a:
    ind=a.index(ele_search)
    print(ele_search,"is in",ind+1,"position.")
else:
    print('The element does not exists')