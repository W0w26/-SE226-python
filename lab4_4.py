dictionary = {}

for i in range(1, 31):
    if i == 1:
        dictionary[i] = 0
    else:
        dictionary[i] = (i-1) * i

# Question 4 part a
print(dictionary)

# Question 4 part b
for key, value in dictionary.items():
    print(key, value)
# Question 4 part c
total = 0

for value in dictionary.values():
    total += value

print("The sum of all the values in the dictionary is:", total)

# Question 4 part d
for i in range(1, 31):
    if i == 1:
        dictionary[i] = 0
    else:
        dictionary[i] = (i-1) * i

key_to_remove = input("Enter a key to remove from the dictionary: ")

if key_to_remove.isdigit() and int(key_to_remove) in dictionary:
    del dictionary[int(key_to_remove)]
    print("The item with key", key_to_remove, "has been removed from the dictionary.")
else:
    print("Invalid input or key not found in the dictionary.")
    
for key, value in dictionary.items():
    print(key, value)