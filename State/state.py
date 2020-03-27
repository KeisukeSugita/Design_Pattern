# Stateパターン
# 共通のインターフェースを実装する「状態」を表すクラスを実装することで、
# 状態の変化に伴う処理を分割することができる
# 状態の追加・削除はインターフェースを実装するだけでよいため、容易にできる
# 状態ごとの処理が分割されているため、メンテナンスもしやすい

from abc import ABCMeta, abstractclassmethod


# 「状態」インターフェース
class WritingState(metaclass=ABCMeta):
	@abstractclassmethod
	def write(self, text):
		pass


class UpperState(WritingState):
	def write(self, text):
		print(text.upper())


class LowerState(WritingState):
	def write(self, text):
		print(text.lower())


class SwapState(WritingState):
	def write(self, text):
		print(text.swapcase())


class Default(WritingState):
	def write(self, text):
		print(text)


# 状態によって振る舞いが変わるクラス
class TextWriter:
	def __init__(self, text):
		self.text = text
		self.state = Default()

	def set_state(self, state):
		self.state = state

	def write(self):
		self.state.write(self.text)


text_writer = TextWriter('Writing Text')
text_writer.write()

text_writer.set_state(UpperState())
text_writer.write()

text_writer.set_state(LowerState())
text_writer.write()

text_writer.set_state(SwapState())
text_writer.write()