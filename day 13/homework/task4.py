age = int(input("შეიყვანეთ ასაკი: "))
heart_rate = int(input("შეიყვანეთ გულისცემა: "))

if age < 30 and heart_rate < 140:
    print("შეგიძლიათ მეტი ივარჯიშოთ")
elif age >= 30 and heart_rate > 170:
    print("დასვენება გჭირდებათ")
else:
    print("აქტივობის დონე ნორმალურია")