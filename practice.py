# 各段につき二つ目のループで9回掛けている

for number in range(9):
    for number2 in range(9):
        print(str((number+1) * (number2+1)) + " ", end = "")
    print("\n")