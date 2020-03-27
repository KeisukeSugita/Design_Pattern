# Mediatorパターン
# 複数のオブジェクト間お互いに指示を出し合うなど、相互に影響しあう時、
# 「仲介者」を用意し、「仲介者」を介して他の各オブジェクト(同僚)同士のやりとりを行わせることで、
# オブジェクト同士が参照し合わないようにでき、結合度を無くすことができる
# 「多」対「多」だったやりとりを「一」対「多」にできるため分かりやすくなる(Mediator自体が複雑化してしまう場合もあるため注意)

from abc import ABCMeta, abstractclassmethod


# 仲介者役インターフェース
class Mediator(metaclass=ABCMeta):
	@abstractclassmethod
	def consultation(self, component):
		pass


class LoginMediator(Mediator):
	def __init__(self, id_textarea, pw_textarea, button):
		self.button = button
		self.id_textarea = id_textarea
		self.pw_textarea = pw_textarea
		button.mediator = self
		id_textarea.mediator = self
		pw_textarea.mediator = self

	def consultation(self, component):
		if type(component) is TextArea:
			self.update_activeness()
		elif type(component) is Button:
			self.confirm_id_pw()

	def update_activeness(self):
		if bool(self.id_textarea.text) and bool(self.pw_textarea.text):
			print('ボタンがアクティブになりました')
			self.button.activeness = True
		else:
			self.button.activeness = False

	def confirm_id_pw(self):
		if self.id_textarea.text == 'ture id' and self.pw_textarea.text == 'true pw':
			print('ログインしました')
		else:
			print('IDまたはパスワードが違います')


# 同僚役基底クラス
class Colleague:
	def __init__(self):
		self.mediator = None

	def advice(self):
		if self.mediator is not None:
			self.mediator.consultation(self)


class Button(Colleague):
	def __init__(self, name=''):
		super().__init__()
		self.activeness = False
		self.name = name

	def click(self):
		if self.activeness:
			self.advice()
		else:
			print('ボタンがアクティブではありません')


class TextArea(Colleague):
	def __init__(self, name=''):
		super().__init__()
		self.name = name
		self.text = ''

	def change_text(self, text):
		self.text = text
		self.advice()


id_textarea = TextArea('ID')
pw_textarea = TextArea('PW')
button = Button('Login')

# buttonはMediatorに作用しても何もおきない
mediator = LoginMediator(id_textarea, pw_textarea, button)

# IDを入力
id_textarea.change_text('ture id')

# まだアクティブでないため、ボタンをおしてもなにもおきない
button.click()

# PWを入力(ここでボタンがアクティブになる)
pw_textarea.change_text('true pw')
button.click()