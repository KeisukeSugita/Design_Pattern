# Facadeパターンを用いない場合
# 複数のクラスを利用する人が適切に制御する必要がある
# 利用するクラス全てに対して関連を持つため、結合が強くなる

from cup import TeaCup, CoffeeCup
from hotWater import HotWater
from drinkSource import TeaSource, CoffeeSource
from drink import Tea, Coffee


tea_cup = TeaCup()
hot_water = HotWater()
tea_drink_source = TeaSource()
tea = Tea(tea_cup, hot_water, tea_drink_source)
tea.drink()
print('----------------')
coffee_cup = CoffeeCup()
coffee_drink_source = CoffeeSource()
coffee = Coffee(tea_cup, hot_water, tea_drink_source)
coffee.drink()