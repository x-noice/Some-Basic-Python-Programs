n=int(input("Enter the prime numbers you want to print: "))
count=0
num=2
flag=0
while count!=n:
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    if(flag==0):
        print(num)
        count+=1
    num+=1
