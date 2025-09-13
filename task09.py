def main():

    students = [["Ali", 18], ["Vali", 20]]
    change_age = int(input("Alining yoshini O`zgartiring: "))

    # Alining malumotini alohida olvoldim
    ali = students[0]

    # Alining yoshi 18da edi uni listdan ajratib oldim
    age_ali = ali[1]

    # Alining ajratib olingan yoshi yangi input qilingan yoshga uzgartirildi
    age_ali = change_age
    
    # Alining eski yoshini o`rniga yangi yoshi quyildi`
    ali[1] = age_ali

    # students nomli listda Alining yangi ma`lumoti yoshi joylandi`
    students[0] = ali

    # va Alining yangi yoshi bilan dastlabgi list qaytarildi
    print(students)
    
main()

# optimallroq varianti ham bor :

# def main():
#    students = [["Ali", 18], ["Vali", 20]]
#   change_age = int(input("Alining yoshini o‘zgartiring: "))

            # Tug`ridan tug`ri listning ichidagi list indeksiga murojat qildim
#    students[0][1] = change_age 
#    print(students)

#main()
