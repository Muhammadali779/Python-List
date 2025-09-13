def main():
    _list = [1, 3, 5, 7, "Salom", "Ali", "Banan", "Olma", 7.7, 10, 8, 0, "Dunyo", False, True]

    start = int(input("Start range: "))
    stop = int(input("Stop range: "))

    n = len(_list)

    if start >= 0 and stop >= 0:

        if 0 <= start < n and 0 <= stop <= n:
            print("Musbat indekslar slicing:")
            print(_list[start:stop])

        else:
            print("Indeks tanlashda hatolik bor!")

    elif start < 0 and stop < 0: 

        if -n <= start < 0 and -n <= stop <= 0:

            if start < stop: 
                print("Manfiy indekslar slicing:")
                print(_list[start:stop])

            else:
                print("Manfiy indekslarda start stopdan katta bo‘lishi mumkin emas!")
        else:
            print("Indeks tanlashda hatolik bor!")

    else:
        print("Start va Stop ikkalasi ham bir xil turda bo‘lishi kerak (musbat yoki manfiy)!")

main()
