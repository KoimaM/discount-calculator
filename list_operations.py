my_list = []

#appending these elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the value 15 at the second position in the list
my_list.insert(1, 15)  # Position 1 is the second element in the list (0-based index)

# Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")

# Optional: Printing the final list to verify everything
print("Final list:", my_list)
