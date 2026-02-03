print (dir(""))
print(help ("bob".capitalize))
print("heLLowww BOBOOBOB123!!!@@".capitalize())
s="hello world"
print(s.upper())
print(s.lower())
print(help(s.center))
print(s.center(30))
print(s.center( 30, "*"))
#fake xmas tree
for i in range(10):
    s="*"*(2*i+1)
    print(s.center(50))
for i in range(4):#stump
    print("***".center(50))

#find, finds the position of the substring
s="i see a cat. the cat is black. cats are nice"
print(s.find("cat"))# 8 is the first occurrance
print(s.find("dog"))#-1 when it cant be find
print(s.find("cat",10))
pos=0
while True:
    pos=s.find("cat",pos)
    if pos==-1:#we cant find it
        break
    print(f"cat on position,{pos}")
    pos+= 1
print(s.count("cat"))
print(s.replace("cat", "dog"))
print(s.split())
