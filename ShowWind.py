from Food import Food
from Drink import Drink

Cake = Food('ケーキ',300,150)
ChocCake = Food('チョコケーキ',450,300)
CheeseCake = Food('チーズケーキ',350,200)
StrawberryCake = Food('イチゴケーキ',400,250)

Cakes =[Cake,ChocCake,CheeseCake,StrawberryCake]


Coffe = Drink('コーヒー' ,200)
Orange = Drink ('オレンジジュース' , 150)
Cola = Drink('コーラ' , 150)
Tea = Drink('お茶' , 100)

Drinks = [Coffe,Orange,Cola,Tea]

index = 0

for cake_item in Cakes:
    print(str(index) + '. ' + cake_item.info())
    index += 1

index = 0
for drink_item in Drinks:
    print(str(index) + ', ' + drink_item.info())
    index += 1