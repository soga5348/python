"""
問題 :
  以下のルールに基づいて割り勘を計算するプログラムを作成してください
  1.一人当たりの支払額は支払総額を参加人数で割った金額とする
  2.支払総額と参加人数を入力で受け取るようにする
  3.支払いの単位は100円とし、100円未満の金額がある場合は切り上げる
  4.支払額を超過した分は、幹事が受け取ることができる(超過した分を幹事支払額から引く)

  また、プログラムを作成する際、以下の3つの関数を作成すること
  ①int_input関数
    機能:画面に入力を促すメッセージを表示し、入力結果を数値に変換して返す
    引数:入力を促す項目を示す文字列
    戻り値:入力された数値

  ②calc_payment関数
    機能:割り勘の計算をする。ただし、幹事以外の支払額は100円単位に丸めて切り上げる
         例)813→900、1370→1400
    引数:支払総額、参加人数(省略時は2とする)
    戻り値:1人あたりの支払額(100円単位)と幹事支払額

  ③show_payment関数
    機能:渡された引数を見やすく表示する
         例)***支払額***
            1人あたり○○円(○○人)、幹事は○○円です
    引数:支払額、幹事支払額、参加人数(省略時は2とする)
    戻り値:なし
"""


import division

sum_member = division.int_input("参加人数")                                #参加人数の値を受け取る
print(sum_member)

sum_payment = division.int_input("支払い金額")                             #支払い金額の値を受け取る
print(sum_payment)


test_two = float(sum_payment)/float(sum_member)                  #test2の保存

one_payment = division.calc_payment(sum_payment,sum_member)                #一人あたりの支払い金額の算定

leader_payment = float(one_payment) - ((100 - test_two%100) * int(sum_member))  #幹事が支払う金額の算定

division.show_payment(one_payment,sum_member,leader_payment)



