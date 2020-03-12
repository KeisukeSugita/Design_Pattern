# TemplateMethodパターン
# スーパークラスで抽象メソッドを定義して処理の枠組みを決める
# 処理を正しい順番で実行させることができる
# 関数を継承によって差し替えることで振る舞いを変えることができ、拡張性が高い

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

	# TemplateMethod　飲み物を作る流れを定めている
	def make(self):
		self.prepare_cup()
		self.boil_hot_water()
		self.set_source_of_drink()
		self.pour_hot_water()
		print('完成です')
		print('----------------')


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
tea_maker.make()

coffee_maker = CoffeeMaker()
coffee_maker.make()