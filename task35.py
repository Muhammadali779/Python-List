short_len = []
average_len = []
long_len = []

while True:
    elements = input("Ro`yxatga element kiriting: ")

    if elements.lower() == "stop":
        break
    
    if 0 < len(elements) <=3:
        short_len.append(elements)
    
    elif 4 <= len(elements) <=6:
        average_len.append(elements)
    
    elif len(elements) > 6:
        long_len.append(elements)
    

print(f"""
    3 ta harfdan kam bo`lgan so`zlar: {short_len}
    4 - 6 ta harflardan iborat so`zlar: {average_len}
    6 ta harfdan kup bulgan so`zlar: {long_len}
""")