from abc import ABCMeta, abstractclassmethod

class Cup:
	@abstractclassmethod
	def prepare(self):
		pass


class TeaCup(Cup):
	def prepare(self):
		print('ティーカップが用意されました')


class CoffeeCup(Cup):
	def prepare(self):
		print('コーヒーカップが用意されました')