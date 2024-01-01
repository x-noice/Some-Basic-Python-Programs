str_1 = input('Enter a string: ')
while True:
    choice = int(input('What task would you like to perform?\n[1]Check palindrome\n[2]Count no. of words\n[3]Count occurence of substring\n[4]No. of words starting with a vowel.\n[5]Exit\nEnter your choice: '))
    if(choice==1):
        temp_str = ''
        str_1_copy = str_1.lower()
        for i in range(len(str_1_copy)-1,-1,-1):
            temp_str = temp_str + str_1_copy[i]
        if(temp_str==str_1_copy):
            print('The string is a palindrome.')
        else:
            print('The string is not a palindrome.')
    elif(choice==2):
        count_words = 0
        start_val = 0
        # Get the index of first occurence of a non-blank character
        for i in range(0,len(str_1)):
            if(str_1[i]!=' '):
                start_val = i
                break
        # Check for no. of blank spaces
        for i in range(start_val,len(str_1)):
            if(str_1[i]==' ' and str_1[i+1]!=' '):
                count_words+=1
        count_words+=1
        print('No. of words =',count_words)
    elif(choice==3):
        substr = input('Enter a substring you would like to count: ')
        print(f"Count of '{substr}' is",str_1.count(substr))
    elif(choice==4):
        #Get words in form of a list
        words = str_1.split()
        count_vow_words=0
        for i in words:
            # Check if word is starting with a vowel or not
            if(i.isalpha() and i[0] in 'AEIOUaeiou'):
                count_vow_words+=1
        print('No. of words starting with a vowel =',count_vow_words)
    elif(choice==5):
        break