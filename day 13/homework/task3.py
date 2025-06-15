age = int(input("შეიყვანეთ ასაკი: "))
hour = int(input("შეიყვანეთ საათი (0-დან 23-მდე): "))

if age < 18 and hour >= 22:
    print("დროა დაძინების")
elif age >= 60 and hour >= 21:
    print("დასვენება რეკომენდებულია")
else:
    print("შეგიძლიათ გააგრძელოთ აქტივობა")