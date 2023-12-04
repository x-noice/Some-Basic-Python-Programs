while True:
    choice = int(input('Which operation would you like to perform?\n[1]Area of a circle\t[2]Circumference of a circle\t[3]Area of a rectangle\t[4]Perimeter of a rectangle\nEnter you choice: '))
    if(choice==1):
        import circle_area
        area = circle_area.circle_area()
        print('Area of circle:',area,'sq.units.')
    elif(choice==2):
        import circle_circumference
        circumference = circle_circumference.circle_circumference()
        print('Circumference of circle:',circumference,'units.')
    elif(choice==3):
        import rectangle_area
        rectangle_area = rectangle_area.rectangle_area()
        print('Area of rectangle:',rectangle_area,'sq.units.')
    elif(choice==4):
        import rectangle_perimeter
        perimeter = rectangle_perimeter.perimeter()
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