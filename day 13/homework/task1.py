name = int(input("შემოიტანე სისტოლური წნევა: "))
name1 = int(input("შემოიტანე დიალოტური წნევა: "))

if name > 140 or name1 > 90:
    print("მაღალი წნევა")
elif name < 90 or name1 < 60:
    print("დააბლი წნევა")
    print(("სხვა შემთხვევაში წნევა ნორმარულია"))