flag = True # True False判定をする為に宣言する
information = dict() # 空辞書の生成
while flag:
    temp = input('気温を入力してください')
    time = input('時間を入力してください')
    information[time] = temp # 辞書の紐付けの完了
    print(time + '時の気温は' + information[time] + '°Cです')
    
    while True: # Error処理をするためにWhile文の作成
        next = input('まだ入力しますか？（Y or Nで）')
        if next == 'Y':
            flag = True
            break
        elif next == 'N':
            flag = False
            break
        else:
            print('ERROR')
        
print(information)

