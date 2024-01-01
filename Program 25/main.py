import rectangle
import circle
while True:
    choice = int(input('Which operation would you like to perform?\n[1]Area of a circle\n[2]Circumference of a circle\n[3]Area of a rectangle\n[4]Perimeter of a rectangle\nEnter you choice: '))
    if(choice==1):
        area = circle.circle_area()
        print('Area of circle:',area,'sq.units.')
    elif(choice==2):
        circumference = circle.circle_circumference()
        print('Circumference of circle:',circumference,'units.')
    elif(choice==3):
        rectangle_area = rectangle.rectangle_area()
        print('Area of rectangle:',rectangle_area,'sq.units.')
    elif(choice==4):
        perimeter = rectangle.perimeter()
        print('Perimeter of rectangle:',perimeter,'units.')
    else:
        print('Please enter a valid response.')
        continue
    print('-'*16)
    con_choice=int(input('Would you like to perform another operation?\n[1]Yes\t[2]No\nEnter you choice: '))
    if(con_choice==1):
        print('-'*16)
        continue
    else:
        break