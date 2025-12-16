'''# Creating a list
numbers = [10, 20, 30, 40, 50]

# Display list
print("Original List:", numbers)

# Append an element
numbers.append(60)
print("After append:", numbers)

# Insert an element at a position
numbers.insert(2, 25)
print("After insert:", numbers)

# Remove an element
numbers.remove(40)
print("After remove:", numbers)

# Pop last element
numbers.pop()
print("After pop:", numbers)


# Sorting list
numbers.sort()
print("Sorted list:", numbers)'''


# List is used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti"]

# Access elements
print(food[0])    # pizza
print(food[3])    # spaghetti

# Update element
food[0] = "sushi"
print(food[0])    # pizza updated to sushi

# Add an element
food.append("ice-cream")

# Remove a specific element
food.remove("hotdog")

# Remove last element
food.pop()

# Remove element by index
food.pop(1)

# Insert element at index
food.insert(0, "cake")

# Sort the list
food.sort()
print("sorted list: ",food)

# Display elements using loop
for item in food:
    print(item)

# Clear the list
food.clear()

