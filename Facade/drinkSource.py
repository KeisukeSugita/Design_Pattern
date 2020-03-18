# 飲み物の素
class DrinkSource:
		pass


class TeaSource(DrinkSource):
	def __init__(self):
		print('ティーバッグをカップに入れます')


class CoffeeSource(DrinkSource):
	def __init__(self):
		print('ドリップバッグをカップに取り付けます')