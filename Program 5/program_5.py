marks1 = int(input("Enter the marks of 1 subject: "))
marks2 = int(input("Enter the marks of 2 subject: "))
marks3 = int(input("Enter the marks of 3 subject: "))
print("Average marks:", round((marks1+marks2+marks3)/3, 2))
percentage = (marks1+marks2+marks3)/300*100
round_percentage = round(percentage)
print("Percentage: ", round_percentage,'%',sep='')
if round_percentage >= 80:
    print("Grade A", "level 4, above agency-normalized standards")
elif round_percentage >= 70 and round_percentage <= 79:
    print("Grade B", "level 3, at agency-normalized standards")
elif round_percentage >= 60 and round_percentage <= 69:
    print("Grade C", "level 2, below,but approaching agency-normalized standards")
elif round_percentage >= 50 and round_percentage <= 59:
    print("Grade D", "level 1, well below agency-normalized standards")
elif round_percentage >= 40 and round_percentage <= 49:
    print("Grade E", "level 1-, too below agency-normalized standards")
elif round_percentage <= 39:
    print("Grade R", "Remedial standards")
else:
    print('An error occurred.')