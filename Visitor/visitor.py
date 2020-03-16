# Visitorパターン
# データ構造と処理を分離することを目的としたパターン
# 訪問者役(Visitor)に処理を実装することで、受け入れ役(Acceptor)から独立した開発ができる
# 新しい処理を追加したいときは新しいVisitorを作るだけ
# データ仕様が変わらず、データに対する処理に複雑性や拡張性が求められる場合に有効的

from abc import ABCMeta, abstractclassmethod


# 訪問者役(Visitor)インターフェース
class Contractor(metaclass=ABCMeta):
	@abstractclassmethod
	def visit(self):
		pass


# 訪問者役(Visitor)水道工事業者クラス
class WaterworksContractor(Contractor):
	def visit(self, acceptor):
		if type(acceptor) is Home:
			print(f'{acceptor.location}に行きます')
			print(f'{acceptor.failure_point}の水道工事をします')
		elif type(acceptor) is Company:
			print(f'{acceptor.location}に行きます')
			print(f'{acceptor.failure_floor}の水道工事をします')


# 訪問者役(Visitor)電気工事業者クラス
class ElectricalContractor(Contractor):
	def visit(self, acceptor):
		if type(acceptor) is Home:
			print(f'{acceptor.location}に行きます')
			print(f'{acceptor.failure_point}の電気工事をします')
		elif type(acceptor) is Company:
			print(f'{acceptor.location}に行きます')
			print(f'{acceptor.failure_floor}の電気工事をします')


# 受け入れ役(Acceptor)インターフェース
class Acceptor(metaclass=ABCMeta):
	@abstractclassmethod
	def accept(self, contractor):
		pass


# 受け入れ役(Acceptor)家クラス
class Home(Acceptor):
	def __init__(self):
		self.location = '神奈川県〇〇市××区'
		self.failure_point = '台所'

	def accept(self, contractor):
		contractor.visit(self)


# 受け入れ役(Acceptor)会社クラス
class Company(Acceptor):
	def __init__(self):
		self.location = '神奈川県□□市〇〇区'
		self.failure_floor = '16F'

	def accept(self, contractor):
		contractor.visit(self)


home = Home()
home.accept(WaterworksContractor())
home.accept(ElectricalContractor())

company = Company()
company.accept(WaterworksContractor())
company.accept(ElectricalContractor())