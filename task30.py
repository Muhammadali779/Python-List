elements = []
palindom_list = []

for i in range(1, 6):
    new_element = input("Ro`yxat uchun Matn kiriting: ")
    elements.append(new_element)

print(elements)

for n in elements:
    
    if n.lower()[::-1] == n.lower():
        palindom_list.append(n)

print(palindom_list)