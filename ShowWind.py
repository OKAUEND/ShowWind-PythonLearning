from Food import Food

Cake = Food('ケーキ',300,150)
ChocCake = Food('チョコケーキ',450,300)
CheeseCake = Food('チーズケーキ',350,200)
StrawberryCake = Food('イチゴケーキ',400,250)

Cakes =[Cake,ChocCake,CheeseCake,StrawberryCake]
index = 0

for cake_item in Cakes:
    print(str(index) + '. ' + cake_item.info())