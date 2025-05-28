print("1-დან 10-მდე:")
i = 1
while i <= 10:
    print(i)
    i += 1

print()

print("10-დან 1-მდე:")
i = 10
while i >= 1:
    print(i)
    i -= 1

print()

count = 0
while count < 3:
    print("ეს არის while ციკლის სხეული")
    count += 1

print()

correct_password = "python123"
entered_password = input("შეიყვანეთ პაროლი: ")

while entered_password != correct_password:
    entered_password = input("პაროლი არასწორია, სცადეთ თავიდან: ")

print("პაროლი სწორია! წვდომა მიღებულია.")

print()

n = int(input("შეიყვანეთ რიცხვი n: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("რიცხვების ჯამი 1-დან", n, "-მდე არის:", total)