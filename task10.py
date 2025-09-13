def main():
    
    fruits = ["Olma", "Anor", "Banan", "Uzum"]

    print(f"Hozirgi ro'yxat: \n{fruits}")

    
    choise_index = int(input("Qaysi indeksni o'zgartirmoqchisiz? (0-3): "))
    new_element = input("Yangi elementni kiriting: ")


    if 0 <= choise_index < len(fruits):
        fruits[choise_index] = new_element
        print(f"Yangilangan ro'yxat: \n{fruits}")

    else:
        print("Xato: bunday indeks yo'q!")

main()
