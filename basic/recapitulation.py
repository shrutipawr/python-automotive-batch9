
'''***What is Scripting?
Scripting is the process of writing small programs  that are executed by an interpreter to automate tasks
and control applications without compilation.


***Difference between Scripting and Programming

Scripting	                           Programming

Interpreted language	               Compiled language
Used for automation & small tasks	   Used for large software development
Executes line by line	               Converted to machine code

***Unique Features of Python
      Simple and easy to learn
      Interpreted language
      High-level language
      Platform independent
      Supports scripting and programming'''


#  Data Types: Data types specify the type of data stored in a variable.

a = 10
b = 2.5
c = "Python"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''Output

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>'''

# Type Casting: Type casting converts one data type into another.

a = "100"
b = int(a)
print(b + 20)

#Output=120

# Input and Output in Python: Input allows user data entry, output displays results

name = input("Enter name: ")
print("Hello", name)

'''Output

Enter name: Ram
Hello Ram'''

# for Loop: for loop is used to repeat a block of code a fixed number of times.

for i in range(1, 6):
    print(i)

'''Output
1
2
3
4
5'''

# while Loop: while loop executes as long as the condition is true.
i = 1
while i <= 3:
    print(i)
    i += 1

'''Output
1
2
3'''

#break Statement: break stops the loop immediately.

for i in range(1, 6):
    if i == 3:
        break
    print(i)

'''Output
1
2'''




# continue Statement :continue skips the current iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

'''Output
1
2
4
5'''






