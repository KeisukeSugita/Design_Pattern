# Stateパターンを利用しない場合
# 状態によってif文で処理を分岐させる必要があるため、
# 状態の追加・削除を行いたいときはif文を書き換える必要がある
# 見通しが悪くなり、メンテナンスもしづらくなってしまう

UPPER = 'Upper'
LOWER = 'Lower'
SWAP = 'Swap'
DEFAULT = 'Default'


class TextWriter:
	def __init__(self, text):
		self.text = text
		self.state = DEFAULT

	def set_state(self, state):
		self.state = state

	def write(self):
		if self.state is DEFAULT:
			print(self.text)
		
		elif self.state is UPPER:
			print(self.text.upper())
		
		elif self.state is LOWER:
			print(self.text.lower())
		
		elif self.state is SWAP:
			print(self.text.swapcase())


text_writer = TextWriter('Writing Text')
text_writer.write()

text_writer.set_state(UPPER)
text_writer.write()

text_writer.set_state(LOWER)
text_writer.write()

text_writer.set_state(SWAP)
text_writer.write()