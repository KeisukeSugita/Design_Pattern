# Mementoパターン
# インスタンスのあるときの状態を保存しておくことで、
# 状態が変化しても保存した時の状態を復元することができる
# 以下のTextEditorとMementoのデータは直接書き換えることができないため、
# カプセル化を破壊せずに状態の復元を行うことができる

class TextEditor:
	def __init__(self):
		self.__content = ''
		self.__content_color = 'Black'

	def input_text(self, text, color):
		self.__content += f'{text}\n'
		self.__content_color = color

	def save(self):
		return TextEditorMemento(self.__content, self.__content_color)

	def restore(self, memento):
		self.__content = memento.get_content()
		self.__content_color = memento.get_content_color()

	def output_text(self):
		print(self.__content)
		print(f'(color:{self.__content_color})')


class TextEditorMemento:
	def __init__(self, content, color):
		self.__content = content
		self.__content_color = color

	def get_content(self):
		return self.__content

	def get_content_color(self):
		return self.__content_color


mementos = {}
text_editor = TextEditor()

text_editor.input_text('1行目', 'Red')
mementos['1行目まで'] = text_editor.save()

text_editor.input_text('2行目', 'Blue')
mementos['2行目まで'] = text_editor.save()

text_editor.input_text('3行目', 'Green')
mementos['3行目まで'] = text_editor.save()

text_editor.restore(mementos['2行目まで'])
text_editor.output_text()
print('----------------')

text_editor.restore(mementos['1行目まで'])
text_editor.output_text()
print('----------------')

text_editor.restore(mementos['3行目まで'])
text_editor.output_text()