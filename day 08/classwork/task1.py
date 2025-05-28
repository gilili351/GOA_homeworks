print("1-დან 10-მდე:")
for i in range(1, 11):
    print(i)

print()

print("10-დან 1-მდე:")
for i in range(10, 0, -1):
    print(i)

print()

count = 0
while count < 3:
    print("ეს არის while ციკლის სხეული")
    count += 1

print()

correct_password = "python123"
for attempt in range(5):
    entered_password = input("შეიყვანეთ პაროლი: ")
    if entered_password == correct_password:
        print("პაროლი სწორია! წვდომა მიღებულია.")
        break
    else:
        print("პაროლი არასწორია.")
else:
    print("ცდების ლიმიტი ამოიწურა.")

print()

n = int(input("შეიყვანეთ რიცხვი n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("რიცხვების ჯამი 1-დან", n, "-მდე არის:", total)