def int_input(msg):
    return int(input(msg + "を入力してください>>"))

def calc_payment(amount, people = 2):

    # 参加者の支払額を求める
    div_num = amount / people
    pay = int((div_num / 100)) * 100
    if pay < div_num:
        pay += 100

    # 幹事の支払額を求める
    pay_secretary = amount - pay * (people - 1)

    return pay, pay_secretary

def show_payment(pay, pay_secretary, people = 2):
    print("***支払額***")
    print("参加人数" +str(people) + "人で、一人当たり" + str(pay) + "円で、幹事は" + str(pay_secretary) + "円です")

# 支払総額、参加人数の入力
amount = int_input("支払総額")
people = int_input("参加人数")

# 参加者と幹事の支払額を求める
pay, pay_secretary = calc_payment(amount, people)

# 結果の表示
show_payment(pay, pay_secretary, people)