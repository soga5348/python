"""
ファイル名 : python_exercise.py
作者: sasaki

- 目次 -
・第1問
・第2問
・第3問
・第4問
・第5問
・第6問

- 更新履歴 -
2022/2/25 新規作成
"""

"""
●第1問
  目安 : python_lesson_1.py終了
  問題 :
  入力された身長(m)、体重(kg)をもとにBMIを計算して表示するプログラムを作成してください
  最後の表示は「身長○○m、体重○○kgのBMIは○○です」としてください
  身長と体重の○○は実際に入力された値を、BMIの○○は計算で求めたBMIを表示するようにしてください
  BMIは「体重÷身長÷身長」で求められます
"""
height = input("身長を入力してください(m)>>")
weight = input("体重を入力してください(kg)>>")

bmi = float(weight) / float(height) / float(height)

print("身長" + height + "m、体重" + weight + "kgのBMIは" + str(bmi) + "です")

"""
●第2問
  目安 : python_lesson_2.py終了
  問題 :
  入力された整数が偶数か奇数かを判定するプログラムを作成してください
  偶数の場合は「偶数です」、奇数の場合は「奇数です」と表示してください
"""
number = int(input("整数を入力してください>>"))

if number % 2 == 0:
    print("偶数です")
else:
    print("奇数です")

"""
●第3問
  目安 : python_lesson_2.py終了
  問題 :
  コンピュータとじゃんけんをするプログラムを作成してください
  以下が条件です
  1.自分の名前を入力できるようにしてください
  2.自分が出す手を入力できるようにしてください
    1が入力されたらグー、2ならチョキ、3ならパーとしてください
  3.コンピュータは必ずチョキを出すようにしてください
  4.「○○は○○を出しました」と表示した後に勝敗を表示してください
    最初の○○は入力した自分の名前、後の○○は自分が出した手を表示してください
  5.自分が出す手を入力する際に、1,2,3以外が入力されたら「正しい手を入力してください」と表示してください
"""
name = input("あなたの名前を入力してください>>")
hand = input("何を出しますか？(1:グー 2:チョキ 3:パー)>>")

print("コンピュータはチョキを出しました")

if hand == "1":
    print(name + "はグーを出しました")
    print(name + "の勝ちです")
elif hand == "2":
    print(name + "はチョキを出しました")
    print("あいこです")
elif hand == "3":
    print(name + "はパーを出しました")
    print(name + "の負けです")
else:
    print("正しい手を入力してください")

"""
●第4問
  目安 : python_lesson_4.py終了
  問題 :
  九九を計算して表示するプログラムを作成してください
  段が変わるごとに改行してください
"""
for i in range(0, 9):
  for j in range(0, 9):
      print(str((i + 1)  * (j + 1)) + " ", end="")
  print("")

"""
●第5問
  目安 : python_lesson_4.py終了
  問題 :
  時間と気温を入力して表示するプログラムを表示してください
  また、入力された時間をキー、気温を値とする辞書を作成してください

  また、時間と気温が入力された後、時間と気温の入力を続けるかどうか選択できるようにしてください
  続けるが選択されたら再度入力できるようにし、終了が選択されたら入力を終了してください
  入力が終了となったら、作成した辞書の内容を順番に「○○時の気温は○○℃です」と表示してください
"""
data_dict = dict()

while True:
    time = input("時間を入力してください>>")
    temp = input("気温を入力してください>>")

    data_dict[time] = temp

    is_stop = input("まだ入力しますか?(y/n)>>")
    if is_stop == "y":
        continue
    else:
        break

for data in data_dict:
    print(data + "時の気温は" + data_dict[data] + "℃です")

"""
●第6問
  目安 : python_lesson_5.py終了
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