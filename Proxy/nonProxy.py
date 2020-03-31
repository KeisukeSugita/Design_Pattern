# Proxyパターンを利用しない場合
# 用意するのに時間がかかるオブジェクトを必ず作成する必要がある

import time


class Cook:
	def __init__(self):
		time.sleep(5)
		self.foodstuff_is_ready = False
		self.foodstuff_is_cut = False
		print('---シェフが到着しました---')

	def prepare_foodstuff(self, dish_name):
		print(f'{dish_name}を作るための食材を用意します')
		self.foodstuff_is_ready = True

	def cut_foodstuff(self):
		print('食材を切り分けます')
		self.foodstuff_is_cut = True

	def stir_fry(self):
		print('食材を炒めます')

	def serve_on_plate(self):
		print('盛り付けて完成です')
		self.foodstuff_is_ready = False
		self.foodstuff_is_cut = False


cook = Cook()

cook.prepare_foodstuff('サラダ')
cook.cut_foodstuff()
cook.serve_on_plate()

print('====================')

cook.prepare_foodstuff('チャーハン')
cook.cut_foodstuff()
cook.stir_fry()
cook.serve_on_plate()
