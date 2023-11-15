word = input('Enter a word: ')
letter = input('Enter a letter you want to count the occurence of: ')
rev_word = '' #Reversed word
count=0
#print out each of the letters of the word
for i in word:
    print(i)
#print out each of the letters of the (same) word in reverse order
print('Letters in reversed order')
for i in range(len(word)-1,-1,-1):
    print(word[i])
    rev_word=rev_word + word[i]
print('Reversed word:',rev_word)
# letter count
for i in word:
    if(i==letter):
        count+=1
print(f'Count of {letter} =',count)