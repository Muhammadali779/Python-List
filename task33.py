list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7]

elements = []

if len(list1) > len(list2):
    max_list = list1
    min_list = list2


for i in min_list:
    if i in max_list:
        elements.append(i)

print(elements)