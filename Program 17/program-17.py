list_1 = []
size = int(input('Enter the no. of observations: '))
for i in range(size):
    el = eval(input('Enter the element: '))
    list_1.append(el)
task = int(input('What task would you like to perform?\nMedian[1]    Mode[2]    Range[3]\n'))
if(task==1):
    if(size%2==0):
        median = (list_1[int((size/2)-1)] + list_1[int(((size/2)+1)-1)])/2
        print('Median =',median)
    elif(size%2!=0):
        median = list_1[int((size+1)/2)-1]
        print('Median =',median)
    else:
        print('An error occurred in calculating Median.')
elif(task==2):
    counter = 0
    mode=[]
    for i in list_1:
        curr_frequency = list_1.count(i)
        if(curr_frequency>counter):
            counter=curr_frequency
            mode.append(i)
        elif(curr_frequency==counter):
            if(i not in mode):
                mode.append(i)
    print('Mode',*mode,sep=', ')
elif(task==3):
    print('Range =',max(list_1)-min(list_1))
else:
    print('An error occured.')
