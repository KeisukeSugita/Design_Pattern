# Proxyパターン
# オブジェクトの代理を提供することで、オブジェクトへのアクセスを制御するパターン
# 代理人と本人が共通のインターフェースを実装し、
# 本人でなくてもできる処理を代理人に任せ、代理人が出来ない処理を本人が行う
# 代理人はメモリの大きなオブジェクトやネットワーク接続など、別の物のインターフェースとして機能する

from abc import ABCMeta, abstractclassmethod
import time


class ICook(metaclass=ABCMeta):
	@abstractclassmethod
	def prepare_foodstuff(self, dish_name):
		pass

	@abstractclassmethod
	def cut_foodstuff(self):
		pass

	@abstractclassmethod
	def stir_fry(self):
		pass

	@abstractclassmethod
	def serve_on_plate(self):
		pass


# シェフの代理人　食材の準備とカット、盛り付けができる
class CookProxy(ICook):
	def __init__(self):
		self.__cook = None
		self.foodstuff_is_ready = False
		self.foodstuff_is_cut = False

	# 代理人が行える処理
	def prepare_foodstuff(self, dish_name):
		print(f'{dish_name}を作るための食材を用意します')
		self.foodstuff_is_ready = True

	# 代理人が行える処理
	def cut_foodstuff(self):
		print('食材を切り分けます')
		self.foodstuff_is_cut = True

	# 本人しか出来ない処理
	def stir_fry(self):
		if self.__cook is None:
			print('---シェフを呼びます---')
			self.__cook = Cook()
		self.__cook.stir_fry()

	def serve_on_plate(self):
		print('盛り付けて完成です')
		self.foodstuff_is_ready = False
		self.foodstuff_is_cut = False


# シェフ本人　すべての作業ができる
class Cook(ICook):
	def __init__(self):
		time.sleep(5)
		print('---シェフが到着しました---')

	def prepare_foodstuff(self, dish_name):
		print(f'{dish_name}を作るための食材を用意します')

	def cut_foodstuff(self):
		print('食材を切り分けます')

	def stir_fry(self):
		print('食材を炒めます')

	def serve_on_plate(self):
		print('盛り付けて完成です')


cook = CookProxy()

cook.prepare_foodstuff('サラダ')
cook.cut_foodstuff()
cook.serve_on_plate()

print('====================')

cook.prepare_foodstuff('チャーハン')
cook.cut_foodstuff()
cook.stir_fry()
cook.serve_on_plate()
