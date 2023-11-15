str_1 = input('Enter a string: ')
v_c=0;c_c=0;u_c=0;l_c=0 # Vowel count, consonants count, uppercase count, lowercase count
for i in str_1:
    if(i.isalpha()):
        if(i in 'AEIOUaeiou'):
            v_c+=1
        else:
            c_c+=1
        if(i.isupper()):
            u_c+=1
        else:
            l_c+=1
print('No. of vowels:', v_c)
print('No. of consonants:', c_c)
print('No. of uppercase characters:', u_c)
print('No. of lowercase characters:', l_c)