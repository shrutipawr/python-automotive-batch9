#slicing=substring
mystring="abcdef-ghijkl"
sub1=mystring[0:6]
print(sub1)
sub2=mystring[7:]
print(sub2)
sub3=mystring[:5]
print(sub3)
sub4=mystring[10]
print(sub4)
sub5=mystring[-5]
print(sub5)

if "a" in mystring:
    print("a is there")

word=mystring.split("-")  
print(word)  