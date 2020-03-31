# Commandパターン
# 命令を1つのオブジェクトで表現する事で詳細な処理をカプセル化し、
# 利用者をReceiverから分離することができる
# 命令の履歴管理の実装が容易にできる
# 新しい命令の追加はCommandインターフェースを実装するだけで簡単に行うことができる

from abc import ABCMeta, abstractclassmethod


class Command(metaclass=ABCMeta):
	@abstractclassmethod
	def execute(self):
		pass

	@abstractclassmethod
	def undo(self):
		pass

	@abstractclassmethod
	def redo(self):
		pass


# 電源ONコマンド
class TurnOn(Command):
	def __init__(self, television):
		self.television = television

	def execute(self):
		self.television.plug_in()
		self.television.push_power_button()
		self.television.turn_on()

	def undo(self):
		self.television.push_power_button()
		self.television.turn_off()
		self.television.unplug()

	def redo(self):
		self.execute()


# 電源OFFコマンド
class TurnOff(Command):
	def __init__(self, television):
		self.television = television

	def execute(self):
		self.television.push_power_button()
		self.television.turn_off()
		self.television.unplug()

	def undo(self):
		self.television.plug_in()
		self.television.push_power_button()
		self.television.turn_on()

	def redo(self):
		self.execute()


# 録画コマンド
class Record(Command):
	def __init__(self, television):
		self.television = television

	def execute(self):
		self.television.record()

	def undo(self):
		self.television.delete_record_data()

	def redo(self):
		self.execute()


# Receiver
class Television:
	def plug_in(self):
		print('コンセントを差し込みます')

	def unplug(self):
		print('コンセントを抜きます')

	def push_power_button(self):
		print('電源ボタンを押します')

	def turn_on(self):
		print('電源がONになりました')

	def turn_off(self):
		print('電源がOFFになりました')

	def record(self):
		print('録画しました')

	def delete_record_data(self):
		print('録画を削除しました')


# Invoker
class TelevisionController:
	commands = []
	redo_commands = []

	def add_command(self, command):
		self.commands.append(command)

	# commandsに追加されているコマンドを実行する
	def execute(self):
		for command in self.commands:
			command.execute()

	# 直前に実行したコマンドを取り消す
	def undo(self):
		if len(self.commands) != 0:
			command = self.commands.pop()
			command.undo()
			self.redo_commands.append(command)

	# 取り消したコマンドを再実行する
	def redo(self):
		if len(self.redo_commands) != 0:
			redo_command = self.redo_commands.pop()
			redo_command.redo()
			self.commands.append(redo_command)


# インスタンス生成
Television_controller = TelevisionController()
television = Television()
turn_on_command = TurnOn(television)
turn_off_command = TurnOff(television)
record_command = Record(television)

# コマンドの追加
Television_controller.add_command(turn_on_command)
Television_controller.add_command(record_command)
Television_controller.add_command(turn_off_command)

# 実行
Television_controller.execute()
# 直前のコマンドを取り消し
Television_controller.undo()
# 1つ前のコマンドを取り消し
Television_controller.undo()
# 直前に取り消したコマンドを再実行
Television_controller.redo()
# 1つ前に取り消したコマンドを再実行
Television_controller.redo()
