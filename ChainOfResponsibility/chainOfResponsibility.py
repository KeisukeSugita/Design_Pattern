# Chain Of Responsibilityパターン
# 処理の責任をそれぞれクラスに分けることで、各クラスの役割を限定することができる
# 各クラスは自分の責任を果たして、残りの処理は次のクラスに任せる実装をする
# 各クラスは共通のインターフェースを実装することで、流れの組み換えも容易にできる
# 要求に対して対応できる人のところへ要求がたらい回し的に流れていくため、
# 柔軟性は高いが処理が遅くなる
# テストしやすくなる

from abc import ABCMeta, abstractclassmethod


# 自らの責任と次の責任者を持つ抽象クラス
class Handler(metaclass=ABCMeta):
	next = None

	def set_next(self, handler):
		self.next = handler
		return handler


	def request(self, print_configuration):
		self.body(print_configuration)
		if self.next != None:
			self.next.request(print_configuration)

	@abstractclassmethod
	def body(self, print_configuration):
		pass


# 印刷部数を確認するクラス
class NumberOfCopysChecker(Handler):
	def body(self, print_configuration):
		print(f'{print_configuration.number_of_copys}部です')


# 印刷を行うクラス
class Printer(Handler):
	def body(self, print_configuration):
		print(f'"{print_configuration.text}"を印刷します')


# ステープルを行うクラス
class Stapler(Handler):
	def body(self, print_configuration):
		if print_configuration.staple_requested:
			print('ステープルします')
		else:
			print('何もしません')


# 印刷設定クラス
class PrintConfiguration:
	def __init__(self, number_of_copys, text, staple_requested):
		self.number_of_copys = number_of_copys
		self.text = text
		self.staple_requested = staple_requested


print_configuration = PrintConfiguration(3, '内容', True)
number_of_copys_checker = NumberOfCopysChecker()
printer = Printer()
stapler = Stapler()
number_of_copys_checker.set_next(printer).set_next(stapler)
number_of_copys_checker.request(print_configuration)