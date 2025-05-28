# task1
# Sequence (მიმდევრობა) — ნიშნავს, რომ კოდი სრულდება ზედიზედ, ხაზობრივად.
# Sequence (მიმდევრობა) — ნიშნავს, რომ კოდი სრულდება ზედიზედ, ხაზობრივად.
# Iteration (იტერაცია) — განმეორებითი მოქმედებაა, მაგ. ციკლის გამოყენებით.
# Selection (არჩევა) — ლოგიკური გადახვევაა, როცა პირობის მიხედვით ერთზე მეტი გზაა.


# task2
# ალგორითმი — ეს არის ნაბიჯ-ნაბიჯ ინსტრუქციების თანმიმდევრობა კონკრეტული ამოცანის შესასრულებლად.
# მაგალითად, ალგორითმი რიცხვის ლუწ/კენტობაზე:

# task3
# and = და
# or = ან

# task4
number = int(input("Enter a number: "))
if (number % 2 == 0 and number > 10) or number == 7:
    print(True)

# task5
print(9 + 9)
print(9.9 + 9.9)
print(True and True)
num1 = "giga"
num2 = "bucxrikidze"
num3 = num1 + num2
print(num3)

# task6
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is leap year")
else:
    print("This is not a leap year")