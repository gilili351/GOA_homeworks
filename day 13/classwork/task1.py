heart = int(input("გულისცემა: "))

if heart > 180:
    print("გულისცემა კარგია")
elif heart > 160 and heart< 170:
    print("გულისცემა ნორმალურია")
elif heart > 160:
    print("გულისცემა ცუდია")