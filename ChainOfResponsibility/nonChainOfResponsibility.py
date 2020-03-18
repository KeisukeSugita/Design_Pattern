# Chain Of Responsibilityパターンを用いない場合
# 1つのメソッドに処理がまとまっているため、状況に応じて必要のない処理や追加したい処理があれば
# それぞれで分岐を作るか、メソッドを分ける必要がある

from abc import ABCMeta, abstractclassmethod


# 印刷を行うクラス
class Printer:
	def print(self, print_configuration):
		print(f'{print_configuration.number_of_copys}部です')

		print(f'"{print_configuration.text}"を印刷します')

		if print_configuration.is_staple:
			print('ステープルします')
		else:
			print('何もしません')


# 印刷設定クラス
class PrintConfiguration:
	def __init__(self, number_of_copys, text, is_staple):
		self.number_of_copys = number_of_copys
		self.text = text
		self.is_staple = is_staple


print_configuration = PrintConfiguration(3, '内容', True)
printer = Printer()
printer.print(print_configuration)