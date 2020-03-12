# Bridgeパターン
# 機能クラスの階層と実装クラスの階層を分けることで、
# 機能の追加や実装の変更を容易に実現することができる
# 後から適応することが難しくないパターン

from abc import ABCMeta, abstractclassmethod

# 文字列を表示するクラス
class Display:
	# DispImpleをメンバに持つことで、DispImpleの実装クラスによってdispの振る舞いを変えることができる
	def __init__(self, disp_imple):
		self.__disp_imple = disp_imple

	def display(self, string):
		self.__disp_imple.display(string)


# 表示の形式にバリエーションを持たせるためのインターフェース
# このインターフェースを実装したクラスのdispをDisplayから利用する
class DispImple(metaclass=ABCMeta):
	@abstractclassmethod
	def display(self, string):
		pass


# 受け取った文字列をそのまま表示するクラス
class NomalDisplay(DispImple):
	def display(self, string):
		print(string)


# 受け取った文字列を'*'で強調して表示するクラス
class EmphasizeDisplay(DispImple):
	def display(self, string):
		print('***{}***'.format(string))


# Displayに繰り返し表示する機能を追加したクラス
class RepeatDisplay(Display):
	def __init__(self, disp_imple):
		super().__init__(disp_imple)

	def repeat_disp(self, string, count):
		while count != 0:
			self.display(string)
			count -= 1


repeat_display = RepeatDisplay(NomalDisplay())
repeat_display.display('abc')
repeat_display.repeat_disp('abc', 3)

print('----------------')

repeat_display = RepeatDisplay(EmphasizeDisplay())
repeat_display.display('abc')
repeat_display.repeat_disp('abc', 3)