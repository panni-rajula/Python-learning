word = input()
if len(word)%2 ==0:
   if word[-1] == ".":
      word = word[:-1]
   elif word[-1] != ".":
        word = word + "."
n = int(len(word)/2)
print(word[(n-1):(n+2)])