while True:
     print("ეს ციკლი უსასრულოდ მიმდინარეობს")


name = input("შეიყვანეთ თქვენი სახელი: ")
print("სახელი გამოჩნდება 10-ჯერ:")
for i in range(10):
    print(f"{i + 1}) {name}")


i = 0  # თავი: საწყისი მნიშვნელობა
while i < 5:  # თავი: პირობის შემოწმება
    print("Hello")  # სხეული: მოქმედება იტერაციისას
    i += 1  # სხეული: ცვლადის განახლება


number = int(input("შეიყვანეთ რიცხვი: "))
while number <= 100:
    number = int(input("რიცხვი უნდა იყოს 100-ზე მეტი. სცადეთ თავიდან: "))
print("მადლობა! სწორი რიცხვი შეყვანილია.")


names = ""
for i in range(5):
    name_input = input(f"{i + 1}-ე სახელი: ")
    if i < 4:
        names += name_input + ", "
    else:
        names += name_input  # ბოლო სახელი აღარ დაამატებს მძიმეს

print("შეყვანილი სახელებია:", names)