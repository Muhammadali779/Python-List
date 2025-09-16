text_list = []


while True:
    element = input("Ro`yxat uchun matn kiriting to`xtatish uchun 'stop' matnini kiriting: ")

    if element.lower() == "stop":
        break
    else:
        text_list.append(element)

if text_list:
    long_text = text_list[0]

    for i in text_list:
        if len(i) > len(long_text):

            long_text = i
            
    print(f"Siz yaratgan ro`yxat: \n{text_list}")    
    print(f"Eng uzun text: {long_text}")
    
else:
    print("Ro`yxat uchun matn kiritilmadi! ")
