'''name = "Alice" #raw data
age = 30 #raw data
print(f"Hello, {name}! You are {age} years old.") 
# Output: Hello, Alice! You are 30 years old.'''

'''item_price = 19.99
item_count = 5
total_cost = item_price * item_count
print(f" your total is ${total_cost:.2f} for {item_count} items.")
#output: Your total is $99.95 for 5 items.

# you can also use the self-documenting
#expression specifier = for debugging
bugs="roaches"
count=13
print(f"Debugging {bugs=} {count=}")
#output: Debugging bugs='roaches' count=13'''

#This prints out: A list:[1,2,3]
mylist = [1,2,3]
print("A list: %s"  % mylist)