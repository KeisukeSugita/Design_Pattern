# AbstractFactoryパターン
# 期待するオブジェクトを作成するために必要となるオブジェクトの生成を専門に行うFactoryクラスを作成する
# 利用側がFactoryを介してDrinkオブジェクトを生成することで、CupとDtinkSourceへの依存を無くせる
# FactoryMethodと比べてテストがしやすい

from abc import ABCMeta, abstractclassmethod
from cup import Cup, CoffeeCup, TeaCup
from drinkSource import TeaSource, CoffeeSource


# Factoryインターフェース
# 飲み物を作るのに必要なCupとDrinkSourceを返すメソッドを持つ
class DrinkFactory(metaclass=ABCMeta):
	#nameよくない
	@abstractclassmethod
	def get_cup(self):
		pass

	@abstractclassmethod
	def get_drink_source(self):
		pass


# 紅茶用のFactoryクラス
class TeaFactory(DrinkFactory):
	def get_cup(self):
		return TeaCup()

	def get_drink_source(self):
		return TeaSource()


# コーヒー用のFactoryクラス
class CoffeeFactory(DrinkFactory):
	def get_cup(self):
		return CoffeeCup()

	def get_drink_source(self):
		return CoffeeSource()


# 飲み物クラス
# CupとDrinkSourceから飲み物を作る
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


# 作成したいオブジェクトの種類が増えた時も、Factoryクラスを増やすだけで事足りる
# 利用側は作成したいオブジェクトのFactoryクラスを用いるだけで期待するオブジェクトを得ることができる
if __name__ == '__main__':
	tea = Drink()
	tea_factory = TeaFactory()
	tea.make(tea_factory.get_cup(), tea_factory.get_drink_source())

	coffee = Drink()
	coffee_factory = CoffeeFactory()
	coffee.make(coffee_factory.get_cup(), coffee_factory.get_drink_source())