# Bridgeパターンを用いない場合
# 機能を追加した場合に、継承先のメソッドに実装を与えることができなくなる
# →既に存在する実装と同じ実装を機能追加したクラスにも与えるためには、
#  機能追加したクラスを継承したクラスをそれぞれ作成しなければならない

from abc import ABCMeta, abstractclassmethod


# 文字列を表示するクラス
class Display(metaclass=ABCMeta):
	@abstractclassmethod
	def disp(self, string):
		pass


# 受け取った文字列をそのまま表示するクラス
class NomalDisplay(Display):
	def disp(self, string):
		print(string)


# 受け取った文字列を'*'で強調して表示するクラス
class EmphasizeDisplay(Display):
	def disp(self, string):
		print('***{}***'.format(string))


# Displayに繰り返し表示する機能を追加したクラス
class RepeatDisplay(Display):
	@abstractclassmethod
	def disp(self, string):
		pass

	def repeat_disp(self, string, count):
		while count != 0:
			self.disp(string)
			count -= 1


# 受け取った文字列を繰り返しそのまま表示するクラス
class RepeatNomalDisplay(RepeatDisplay):
	def disp(self, string):
		print(string)


# 受け取った文字列を繰り返し'*'で強調して表示するクラス
class RepeatEmphasizeDisplay(RepeatDisplay):
	def disp(self, string):
		print('***{}***'.format(string))


repeat_nomal_display = RepeatNomalDisplay()
repeat_nomal_display.disp('abc')
repeat_nomal_display.repeat_disp('abc', 3)

print('----------------')

repeat_emphasize_display = RepeatEmphasizeDisplay()
repeat_emphasize_display.disp('abc')
repeat_emphasize_display.repeat_disp('abc', 3)