from abc import ABCMeta, abstractclassmethod

class DrinkSource(metaclass=ABCMeta):
	@abstractclassmethod
	def prepare(self):
		pass


class TeaSource(DrinkSource):
	def prepare(self):
		print('ティーバッグをカップに入れます')


class CoffeeSource(DrinkSource):
	def prepare(self):
		print('ドリップバッグをカップに取り付けます')