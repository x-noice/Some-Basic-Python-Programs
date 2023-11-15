n = None
s_e = 0
s_o = 0
s_n = 0
perm = 'y'

while(n!=0 and perm=='y'):
    n = eval(input('Enter a number: '))
    if(n!=0):
        perm = input('Do you want to continue?\nYes(y)\tNo(n)')
        
        if(n>0):
            if(n%2 == 0):
                s_e += n
            elif(n%2 !=0):
                s_o += n
            else:
                print('Error occured in n>0')
        elif(n<0):
            s_n += n
        else:
            print('Error occured in checkNum()')
        
        if(perm=='n'):    
            print('Sum of +ve odd no. is', s_o)
            print('Sum of +ve even no. is', s_e)
            print('Sum of -ve no. is', s_n)
        
    elif(n==0):
        print('Since the number entered is 0, the program will be terminated.')
        print('Sum of +ve odd no. is', s_o)
        print('Sum of +ve even no. is', s_e)
        print('Sum of -ve no. is', s_n)

    else:
        print('An error occured.')
