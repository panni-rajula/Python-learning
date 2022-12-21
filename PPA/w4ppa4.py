L = input().split(',')
long_word,length_word='',0
for i in range(len(L)):
    if len(L[i])>length_word:
        long_word=L[i]
        length_word=len(L[i])
print(f"the longest word is{long_word} and its length is {length_word}")