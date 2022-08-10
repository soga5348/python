PLUSS = "+"
MINUSS = "-"
TIMES = "*"
DIVIDE = "/"



a = input("数1を入力してください") #inputで受け取ったものは文字列
b = input("数2を入力してください")
c = input("演算子を入力してください")#演算子はにゅ
if c == PLUSS:
    print(int(a)+int(b))
elif c == MINUSS:
    print(int(a)-int(b))
elif c == TIMES:
    print(int(a)*int(b))
elif c == DIVIDE:
    print(int(a)/int(b))
else:
     print("正しい演算子を入力してください")



