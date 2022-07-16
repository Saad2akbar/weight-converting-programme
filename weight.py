weight = int and float(input("Weight: "))
qna = input('(L)lbs or (K)kg: ')
if qna.upper() == "L":
    converted = weight *  0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
