

my_list = [1, 4, 55, 154, 45, 66, 33, 4, 44]

max_count = 0
for elem in my_list:
    if elem > max_count:
        max_count = elem

print(max_count)