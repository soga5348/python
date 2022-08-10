

def int_input(message):                                         #インプット関数の作成、入力された値を受け取る
    test = input(message + "を入力してください")
    return test

def calc_payment(sum_pay,sum_mem):                                     #一人あたりの支払い金額を計算する関数の作成
    test2 = float(sum_pay)/float(sum_mem)
    test3 = float(test2) + (100 - float(test2)%100)
    return test3

def show_payment(num1,num2,num3):                               #計算した結果を表示させる関数の作成
    return
    print("***支払額***\n" + "一人当たり" + str(num1) +"円" + "(" + str(num2) + ")" + "人" + ",幹事は" + str(num3) + "円です")
