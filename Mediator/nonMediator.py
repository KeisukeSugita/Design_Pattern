# Mediatorパターンを使用しない場合
# オブジェクト同士が直接関係を持ち、お互いの実装を知っている必要があるため、汎用性が低くなってしまう


class Button:
	def __init__(self, textarea_id, textarea_pw):
		self.activeness = False
		self.textarea_id = textarea_id
		self.textarea_pw = textarea_pw

	def update_activeness(self):
		if bool(self.textarea_id.text) and bool(self.textarea_pw.text):
			print('ボタンがアクティブになりました')
			self.activeness = True

	def click(self):
		if self.activeness:
			self.confirm_id_pw()
		else:
			print('ボタンがアクティブではありません')

	def confirm_id_pw(self):
		if self.textarea_id.text == "true id" and self.textarea_pw.text == "true pw":
			print('ログインしました')
		else:
			print('IDまたはパスワードが違います')


class TextArea:
	def __init__(self, name=""):
		self.name = name
		self.text = ""

	def set_button(self, button):
		self.button = button

	def set_text(self, text):
		self.text = text
		self.button.update_activeness()


textarea_id = TextArea("ID")
textarea_pw = TextArea("PW")
button = Button(textarea_id, textarea_pw)
textarea_id.set_button(button)
textarea_pw.set_button(button)

# IDを入力
textarea_id.set_text("true id")

# まだアクティブでないため、ボタンをおしてもなにもおきない
button.click()

# PWを入力(ここでボタンがアクティブになる)
textarea_pw.set_text("true pw")
button.click()