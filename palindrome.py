from string import punctuation

s="Yo! Banana Boy."
#step 1. remove punctuation
#step 2. remove spaces
#step 3. convert upper/lower case
#step 4. compare with the reversed

punctuation= "!.,"
for p in punctuation:
    s=s.replace(p,"") #remove punctuation
print(s)
#now spaces
s=s.replace(" ","")
print(s)
s=s.lower()
print(s)
if s==s[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")