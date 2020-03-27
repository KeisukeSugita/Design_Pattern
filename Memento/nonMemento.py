# Mementoパターンを利用しない場合
# インスタンスのデータにアクセスして保持、上書きする必要があるため、
# 利用者はインスタンスの復元のために保持しているデータを自由に書き換えることができてしまう

class TextEditor:
	def __init__(self):
		self.__content = ''
		self.__content_color = 'Black'

	def input_text(self, text, color):
		self.__content += f'{text}\n'
		self.__content_color = color

	def get_content(self):
		return self.__content

	def set_content(self, content):
		self.__content = content

	def get_content_color(self):
		return self.__content_color

	def set_content_color(self, color):
		self.__content_color = color

	def output_text(self):
		print(self.__content)
		print(f'(color:{self.__content_color})')



saved_contents = {}
saved_content_colors = {}
text_editor = TextEditor()

text_editor.input_text('1行目', 'Red')
saved_contents['1行目まで'] = text_editor.get_content()
saved_content_colors['1行目まで'] = text_editor.get_content_color()

text_editor.input_text('2行目', 'Blue')
saved_contents['2行目まで'] = text_editor.get_content()
saved_content_colors['2行目まで'] = text_editor.get_content_color()

text_editor.input_text('3行目', 'Green')
saved_contents['3行目まで'] = text_editor.get_content()
saved_content_colors['3行目まで'] = text_editor.get_content_color()

text_editor.set_content(saved_contents['2行目まで'])
text_editor.set_content_color(saved_content_colors['2行目まで'])
text_editor.output_text()
print('----------------')

text_editor.set_content(saved_contents['1行目まで'])
text_editor.set_content_color(saved_content_colors['1行目まで'])
text_editor.output_text()
print('----------------')

text_editor.set_content(saved_contents['3行目まで'])
text_editor.set_content_color(saved_content_colors['3行目まで'])
text_editor.output_text()