from abc import ABCMeta, abstractclassmethod


# 飲み物
class Drink(metaclass=ABCMeta):
	def __init__(self, cup, hot_water, drink_source):
		hot_water.pour()

	@abstractclassmethod
	def drink(self):
		pass


class Tea(Drink):
	def __init__(self, cup, hot_water, drink_source):
		super().__init__(cup, hot_water, drink_source)

	def drink(self):
		print('紅茶を飲みました')


class Coffee(Drink):
	def __init__(self, cup, hot_water, drink_source):
		super().__init__(cup, hot_water, drink_source)

	def drink(self):
		print('コーヒーを飲みました')