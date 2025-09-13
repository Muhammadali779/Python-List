def main():

    _list = [1, 3, 5, 7, "Salom", "Ali", "Banan", "Olma", 7.7, 10]
                      #10 - 3 = 7 
    last_3_items = len(_list) - 3
                       # _list[7:] 10tadan oxirgi 3tani chiqaradi
    slice_list = _list[last_3_items:]

    print(slice_list)

main()