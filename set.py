

my_list = [1, 2, 4, 33, 2, 6, 88, 88, 17]
print("Original_list : ",  my_list)

my_set = set(my_list)
print("Unicue list : ", my_set)
summa = sum(my_set)
print("Sum from function", summa)
my_summa = 0
for elem in my_set:
    my_summa = my_summa + elem
print("Sum from cicle ", my_summa)
