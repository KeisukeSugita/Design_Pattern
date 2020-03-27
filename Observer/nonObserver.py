# Observerパターンを利用しない場合
# あるオブジェクト(被観測者)の状態変化を知りたいオブジェクト(観測者)が、
# 観測者は被観測者を観測し続ける必要がある
# 観測者、被観測者を追加していく場合に、実装が分かりにくく複雑になっていってしまう

from abc import ABCMeta, abstractclassmethod
import time
import threading


# 天気リポータークラス
class WeatherReporter:
	def __init__(self, weather):
		self.weather = weather
		self.is_stop_requested = False

	def observe_start(self):
		self.is_stop_requested = False
		while True:
			if self.weather.is_called:
				self.report(self.weather.status)
				time.sleep(0.001)
			if self.is_stop_requested:
				break

	def observe_stop(self):
		self.is_stop_requested = True

	def report(self, weather_status):
		print('----天気リポーター----')
		if weather_status == 'Sunny':
			print('晴天です')
		elif weather_status == 'Rainy':
			print('雨天です')


# 先生クラス
class Teacher:
	def __init__(self, weather):
		self.weather = weather

		self.is_stop_requested = False

	def observe_start(self):
		self.is_stop_requested = False
		while True:
			if self.weather.is_called:
				self.announce(self.weather.status)
				time.sleep(0.001)
			if self.is_stop_requested:
				break

	def observe_stop(self):
		self.is_stop_requested = True

	def announce(self, weather_status):
		print('----先生----')
		if weather_status == 'Sunny':
			print('遠足に行きましょう')
		elif weather_status == 'Rainy':
			print('遠足は中止です')


# 被観測者
class Weather:
	def __init__(self):
		self.status = None
		self.is_called = False

	def set_status(self, weather):
		self.status = weather
		self.is_called = True
		time.sleep(0.0005)
		self.is_called = False


weather = Weather()
weather_reporter = WeatherReporter(weather)
teacher = Teacher(weather)

thread_reporter = threading.Thread(target=weather_reporter.observe_start)
thread_teacher = threading.Thread(target=teacher.observe_start)
thread_reporter.start()
thread_teacher.start()

weather.set_status('Sunny')
print('')
time.sleep(1)
weather.set_status('Rainy')

weather_reporter.observe_stop()
teacher.observe_stop()