# Adapterパターン
# 関連性のないクラス同士を、既存のクラスを変更せずに関連付けできる
# 既存のクラスを、新たなインターフェースを通じて利用できる
# 既存のクラス・インターフェースをアプリケーション固有に使いやすくできる

from abc import ABCMeta, abstractmethod

# 既存のクラス(Adaptee)
# コンソールに出力を行うクラス
class ConsoleWriter:
	# コンソールにmessageを出力する
	def write_to_console(self, message):
		print(message)


# 既存のクラス(Adaptee)
# ファイルに出力を行うクラス
class FileWriter:
	# file_nameファイルにmessageを出力する
	def write_to_file(self, file_name, message):
		file_obj = open(file_name, 'w')
		print(message, file = file_obj)


# 複数の出力方法をまとめて使用するインターフェース(Target)
# このインターフェースのメソッドを使いたい
class IHybridWriter(metaclass = ABCMeta):
	# コンソールとfile_nameファイルにmessageを出力する
	@abstractmethod
	def write(self, file_name, message):
		pass


# ConsoleWriterとFileWriterを継承することで、IHybridWriter.writeを実装するクラス(Adapter)
# is a
class HybridWriter(IHybridWriter, ConsoleWriter, FileWriter):
	def write(self, file_name, message):
		super().write_to_console(message)
		super().write_to_file(file_name, message)

# Adapteeを継承できない場合のAdapter
# has a
'''
class HybridWriter(IHybridWriter):
	def __init__(self)
		console_writer = ConsoleWriter()
		file_writer = FileWriter()
	def write(self, file_name, message):
		console_writer.write_to_console(message)
		file_writer.write_to_file(file_name, message)
'''


hybrid_writer = HybridWriter()
hybrid_writer.write('report.txt', 'message string')

