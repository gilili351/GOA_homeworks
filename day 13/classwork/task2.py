age = int(input("შემოიტანე შენი ასაკი: "))

if -age:
    print("არასწორი ასაკი")
elif age > 13:
    print("ბავშვი")
elif age == 13 and age < 19:
    print("თინეიჯერი")
elif age == 20 < 59:
    print("ზრდასრული")
elif age == 60 or age > 60:
    print("პენსიონერი")