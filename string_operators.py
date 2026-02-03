# + will perform string concatenation
s1 = "hello"
s2 = "bye"
print(s1 + s2)
print(s2 + s1)
print(s1 + " " + s2)

# you can multiply string by an integer
print(3*s2) #nsync song
print(s1 + " " + s2 + "!"*10)

# we can iterate over a string for
for c in s1:
    print(c)

# Exercise
# 1. do the same with a while
i = 0
while i < len(s1):
    print(s1[i])
    i += 1

# 2. i want the result to be hhhhhheeeeelllllloooo
s_new = ""
for c in s1:
    s_new = s_new + c*4
print(s_new)