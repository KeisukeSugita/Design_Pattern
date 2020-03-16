# Compositeパターン
# 容器と中身を同一視する(同一の機能を持たせる)パターン
# 中身の種類が増えた時、共通のインターフェースを実装するだけで事足りる
# 入れ子になる(再帰的な)構造を作るときに有効

from abc import ABCMeta, abstractclassmethod


class Tree(metaclass=ABCMeta):
	@abstractclassmethod
	def cut(self):
		pass


# 「中身」役
class Leaf(Tree):
	def __init__(self, name):
		self.name = name

	def cut(self):
		print('{}を切りました'.format(self.name))


# 「容器」役
# 「容器」を入れることもできる
class Branch(Tree):
	def __init__(self, name):
		self.name = name
		self.list = []

	def add(self, tree):
		self.list.append(tree)

	def cut(self):
		for component in self.list:
			component.cut()

		print('{}を切りました'.format(self.name))


leaf1 = Leaf('leaf1')
leaf2 = Leaf('leaf2')
leaf3 = Leaf('leaf3')
leaf4 = Leaf('leaf4')
branch1 = Branch('branch1')
branch2 = Branch('branch2')

branch1.add(leaf1)
branch1.add(branch2)
branch1.add(leaf4)
branch2.add(leaf2)
branch2.add(leaf3)

branch1.cut()