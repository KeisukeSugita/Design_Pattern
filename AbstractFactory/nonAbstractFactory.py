from abc import ABCMeta, abstractclassmethod
from cup import Cup, CoffeeCup, TeaCup
from drinkSource import TeaSource, CoffeeSource


class Drink:
	def __prepare_cup(self, cup):
		cup.prepare()

	def __set_drink_source(self, drink_source):
		drink_source.prepare()

	def __pour_hot_water(self):
		print('お湯を注ぎます')

	def make(self, cup, drink_source):
		self.__prepare_cup(cup)
		self.__set_drink_source(drink_source)
		self.__pour_hot_water()
		print('完成です')
		print('----------------')


# 一見スッキリしているようにみえるが、CupとDrinkSourceのインスタンスをmainで作成して渡す必要がある
# そのため、紅茶を作ろうとしているのに作る人によって違うCupとDrinkSourceを使ってしまう可能性がある
if __name__ == '__main__':
	tea = Drink()
	tea.make(TeaCup(), TeaSource())

	coffee = Drink()
	coffee.make(CoffeeCup(), CoffeeSource())