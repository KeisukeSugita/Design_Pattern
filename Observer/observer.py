# Observerパターン
# 状態の変化を観察する事を目的としたパターン
# 被観測者から状態の変化を観測者に通知することで実現する
# 観測者、被観測者の追加を容易に行うことができる

from abc import ABCMeta, abstractclassmethod


# 観測者インターフェース
class WeatherObserver(metaclass=ABCMeta):
	@abstractclassmethod
	def update(self, weather):
		pass


# 天気リポータークラス
class WeatherReporter(WeatherObserver):
	def update(self, weather):
		print('----天気リポーター----')
		if weather == 'Sunny':
			print('晴天です')
		elif weather == 'Rainy':
			print('雨天です')


# 先生クラス
class Teacher(WeatherObserver):
	def update(self, weather):
		print('----先生----')
		if weather == 'Sunny':
			print('遠足に行きましょう')
		elif weather == 'Rainy':
			print('遠足は中止です')


# 被観測者
class Weather:
	def __init__(self):
		self.observers = []
		self.status = None

	def add_observer(self, observer):
		self.observers.append(observer)

	def notify_observers(self, weather):
		for observer in self.observers:
			observer.update(weather)

	def set_status(self, weather):
		self.status = weather
		self.notify_observers(self.status)


weather = Weather()
weather_reporter = WeatherReporter()
teacher = Teacher()

weather.add_observer(weather_reporter)
weather.add_observer(teacher)

weather.set_status('Sunny')
print('')
weather.set_status('Rainy')