'''students=[56,100,78,89,65,87,89,55]
pass_students= ["pass" if i>=60 else "failed" for i in students]
print[pass_students]'''





'''# List comprehension is a way to create a new list with less syntax

# Normal method using for loop
squares = []                  # create empty list
for i in range(1, 11):        # loop from 1 to 10
    squares.append(i * i)     # square of each number

print(squares)

# Using list comprehension
squares1 = [i * i for i in range(1, 11)]
print(squares1)

# --------------------------------------------

# Example with condition'''
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# Pass or Fail using list comprehension
pass_students = ["Pass" if i >= 60 else "Fail" for i in students]

print(pass_students)