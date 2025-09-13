def main():

    _list = [1, 2, 4, 3, 11, 6, 7, 55, 9, 11]

    even_index = []

    for i in range(len(_list)):
        if i % 2 == 0:
            even_index += [_list[i]]
        
    print(even_index)

main()