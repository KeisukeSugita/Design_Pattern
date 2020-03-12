# FactoryMethodパターン
# インスタンスを生成するメソッドをオーバーライドすることで、作成するインスタンスを柔軟に選択することができる
# サブクラスで生成するインスタンスを選択できるため

from abc import ABCMeta, abstractclassmethod
from cup import Cup, CoffeeCup, TeaCup


# 飲み物を作るクラス
class DrinkMaker(metaclass = ABCMeta):
	# Factorymethod　飲み物を作るために用意するカップを決めることができる
	@abstractclassmethod
	def create_cup(self):
		pass

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
	def make(self):
		cup = self.create_cup()
		self.prepare_cup(cup)
		self.boil_hot_water()
		self.set_source_of_drink()
		self.pour_hot_water()
		print('完成です')
		print('----------------')


# 紅茶を作るクラス
class TeaMaker(DrinkMaker):
	# ティーカップを用意
	def create_cup(self):
		return TeaCup()
	
	def set_source_of_drink(self):
		print('ティーバッグを入れます')


# コーヒーを作るクラス
class CoffeeMaker(DrinkMaker):
	# コーヒーカップを用意
	def create_cup(self):
		return CoffeeCup()
	
	def set_source_of_drink(self):
		print('ドリップバッグを取り付けます')

	# フックをオーバーライド
	def pour_hot_water(self):
		print('ゆっくりとお湯を注ぎます')


tea_maker = TeaMaker()
tea_maker.make()

coffee_maker = CoffeeMaker()
coffee_maker.make()