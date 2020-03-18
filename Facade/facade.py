# 利用側が詳細な制御を記述する必要がなくなる
# 意図しない呼び出し方でのエラー等を防ぐことができる
# 利用側が呼び出すメソッドを絞ることで、他のクラスと疎結合にできる

from cup import TeaCup, CoffeeCup
from hotWater import HotWater
from drinkSource import TeaSource, CoffeeSource
from drink import Tea, Coffee

TEA = 'TEA'
COFFEE = 'COFFEE'


# Facade(窓口)役 詳細な制御を行ってくれる
class DrinkShop:
	def sell(self, drink_name):
		if drink_name is TEA:
			cup = TeaCup()
			hot_water = HotWater()
			drink_source = TeaSource()
			return Tea(cup, hot_water, drink_source)
		elif drink_name is COFFEE:
			cup = CoffeeCup()
			hot_water = HotWater()
			drink_source = CoffeeSource()
			return Coffee(cup, hot_water, drink_source)


drink_shop = DrinkShop()
tea = drink_shop.sell(TEA)
tea.drink()
print('----------------')
coffee = drink_shop.sell(COFFEE)
coffee.drink()