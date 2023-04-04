divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = {**divided, **we_fall}

print("{:<10} {:<10}".format('Name', 'Age'))
print('-'*20)
for key, value in united_we_stand.items():
    print("{:<10} {:<10}".format(key, value))

del united_we_stand['Nat']
print("{:<10} {:<10}".format('Name', 'Age'))
print('-'*20)
for key, value in united_we_stand.items():
    print("{:<10} {:<10}".format(key, value))

print("{:<10} {:<10}".format('Name', 'Age'))
print('-'*20)
for key in sorted(united_we_stand.keys()):
    print("{:<10} {:<10}".format(key, united_we_stand[key]))

ages = list(united_we_stand.values())
print("Maximum age:", max(ages))
print("Minimum age:", min(ages))