from abc import ABCMeta, abstractclassmethod

class Cup(metaclass=ABCMeta):
	@abstractclassmethod
	def prepare(self):
		pass


class TeaCup(Cup):
	def prepare(self):
		print('ティーカップを用意しました')


class CoffeeCup(Cup):
	def prepare(self):
		print('コーヒーカップを用意しました')