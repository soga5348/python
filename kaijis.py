import random
num  = input('あなたは何を出しますか：')
card = ['皇帝','奴隷','市民','市民','市民']
player_select = num
computer_select = random.choice(card)
print('私のカードは'+player_select+'です')
input('相手のカードをみる：')
print('相手のカードは'+computer_select+'です')
if player_select=='皇帝' and computer_select=='皇帝':
    print('引き分けです')
elif player_select=='皇帝'and computer_select=='市民':
    print('あなたの勝ちです')
elif player_select=='皇帝' and computer_select=='奴隷':
    print('あなたの負けです')
elif player_select=='市民' and computer_select=='皇帝':
    print('あなたの負けです')
elif player_select=='市民' and computer_select=='市民':
    print('引き分けです')  
elif player_select=='市民'and computer_select=='奴隷':
    print('あなたの勝ちです')
elif player_select=='奴隷'and computer_select=='皇帝':
    print('あなたの勝ちです')
elif player_select=='奴隷' and computer_select=='市民':
    print('あなたの負けです')
elif player_select=='奴隷' and computer_select=='奴隷':
    print('引き分けです')
