ls = [45,89,56,789,547,254,346,876,34,109]

max_value = ls[0]
min_value = ls[0]

for num in ls:
    if num > max_value:
        max_value = num
    elif num < min_value:
        min_value = num

print("Maximum value:", max_value)
print("Minimum value:", min_value)