def main():
    list_people = []
    for i in range(1, 4):
        name = input(f"{i} - ismni kiriting: ")
        list_people += [f"{name}"]

    print(list_people)

main()