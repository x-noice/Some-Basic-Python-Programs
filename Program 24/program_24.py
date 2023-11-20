n = int(input('Enter no. of students: '))
student_dict={}
for i in range(n):
    student = input('Enter name: ')
    percentage = input('Enter percentage(%): ')
    student_dict.update({student:percentage})
print(student_dict)
del_student = input('Enter the name you would like to delete: ')
if(del_student in student_dict):
    del student_dict[del_student]
    print(student_dict)
else:
    print('Record doesn\'t exist.')
