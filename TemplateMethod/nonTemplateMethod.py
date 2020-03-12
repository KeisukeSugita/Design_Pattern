# TemplateMethodパターンを用いない場合
# 処理の順番を間違えてしまう可能性がある
# クラス利用側がメソッドを何度も呼び出すことになる
# 複数の処理を一つにまとめてしまった場合、拡張性が無くなる

from abc import ABCMeta, abstractclassmethod

# 飲み物を作るクラス
class DrinkMaker(metaclass = ABCMeta):
	@abstractclassmethod
	def prepare_cup(self):
		pass

	def boil_hot_water(self):
		print('お湯を沸かします')

	@abstractclassmethod
	def set_source_of_drink(self):
		pass

	def pour_hot_water(self):
		print('お湯を注ぎます')


# 紅茶を作るクラス
class TeaMaker(DrinkMaker):
	def prepare_cup(self):
		print('ティーカップを用意します')
	
	def set_source_of_drink(self):
		print('ティーバッグを入れます')


# コーヒーを作るクラス
class CoffeeMaker(DrinkMaker):
	def prepare_cup(self):
		print('コーヒーカップを用意します')
	
	def set_source_of_drink(self):
		print('ドリップバッグを取り付けます')

	# フックをオーバーライド
	def pour_hot_water(self):
		print('ゆっくりとお湯を注ぎます')


tea_maker = TeaMaker()
tea_maker.prepare_cup()
tea_maker.boil_hot_water()
tea_maker.set_source_of_drink()
tea_maker.pour_hot_water()
print('完成です')
print('----------------')

coffee_maker = CoffeeMaker()
coffee_maker.boil_hot_water()
coffee_maker.set_source_of_drink()
coffee_maker.pour_hot_water()
coffee_maker.prepare_cup()
print('完成です')
print('----------------')