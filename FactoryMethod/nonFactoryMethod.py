# FactoryMethodパターンを用いない場合
# インスタンスを渡す必要があるため、利用側が依存するクラスが増える
# クラス利用側がメソッドを何度も呼び出すことになる

from abc import ABCMeta, abstractclassmethod
from cup import Cup, CoffeeCup, TeaCup


# 飲み物を作るクラス
class DrinkMaker(metaclass = ABCMeta):
	def prepare_cup(self, cup):
		cup.prepare()

	def boil_hot_water(self):
		print('お湯を沸かします')

	@abstractclassmethod
	def set_source_of_drink(self):
		pass

	def pour_hot_water(self):
		print('お湯を注ぎます')

	# TemplateMethod　飲み物を作る流れを定めている
	def make(self, cup):
		self.prepare_cup(cup)
		self.boil_hot_water()
		self.set_source_of_drink()
		self.pour_hot_water()
		print('完成です')
		print('----------------')


# 紅茶を作るクラス
class TeaMaker(DrinkMaker):
	def set_source_of_drink(self):
		print('ティーバッグを入れます')


# コーヒーを作るクラス
class CoffeeMaker(DrinkMaker):
	def set_source_of_drink(self):
		print('ドリップバッグを取り付けます')

	# フックをオーバーライド
	def pour_hot_water(self):
		print('ゆっくりとお湯を注ぎます')


tea_maker = TeaMaker()
tea_cup = TeaCup()
tea_maker.make(tea_cup)

coffee_maker = CoffeeMaker()
coffee_cup = CoffeeCup()
coffee_maker.make(coffee_cup)