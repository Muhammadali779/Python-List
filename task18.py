def main():
  # Ro`yxat uzunligi toq bolsa TRUE bulishi kerak ekan shart bo`yicha! 
  # shunga else shart bajarilganda True chiarish kerak! 
    _list = [1, 4, 6, "olma", False, 100, 99.9]

    result = len(_list) % 2 == 0

    if result:
        print(False)
        print("Ro`yxat uzunligi JUFT! ")
    else:
        print(True)
        print("Ro`yxat uzunligi TOQ! ")

    

main()
    
