num = int(input('Please enter a number:\n'))
if(num>0):
    print('Absolute value of number =',num)
elif(num==0):
    print('The value of number =',num)
elif(num<0):
    print('Absolute value of number =', (num*-1))
else:
    print('An error occured.')
