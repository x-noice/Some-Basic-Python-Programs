def markscalc(sub):
    if(sub>100):
        print('Please enter marks of each subject out of 100 only!')
        sub = eval(input('Enter the marks for the subject again: \n'))
        markscalc(sub)
    else:
        return sub

print('Enter marks out of 100 for each and every subject!')
print('-' * 62)
sub_1 = eval(input('Enter the marks for subject 1: \n'))
markscalc(sub_1)
sub_1 = markscalc(sub_1)
print(sub_1)
sub_2 = eval(input('Enter the marks for subject 2: \n'))
markscalc(sub_2)
sub_3 = eval(input('Enter the marks for subject 3: \n'))
markscalc(sub_3)
sub_4 = eval(input('Enter the marks for subject 4: \n'))
markscalc(sub_4)
sub_5 = eval(input('Enter the marks for subject 5: \n'))
markscalc(sub_5)

percentage = ((sub_1 + sub_2 + sub_3 + sub_4 + sub_5)/500) * 100
print('Total percentage scored = ' , percentage, '%', sep = '')
