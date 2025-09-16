list1 = [1, 2, 3]
list2 = [4, 5, 6]

if len(list1) == len(list2):
    _list1 = list2.copy()
    _list2 = list1.copy()

    print(f"""
    Old List1: {list1} ===> Copied List2 to list1: {_list1} 
    Old List2: {list2} ===> Copied List1 to list2: {_list2} 
""")
    
else:
    print("Listdagi elementlar soni teng emas! ")

