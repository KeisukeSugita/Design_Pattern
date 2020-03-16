# Compositeパターンでない場合
# 中身の種類が増えた時、容器は新たな中身に対する実装を追加する必要が出てくる
# 中身の種類が増えるにしたがって容器の実装が複雑になり、見通しが悪くなる

# 「中身」役
class Leaf:
	def __init__(self, name):
		self.name = name

	def cut(self):
		print('{}を切りました'.format(self.name))


# 「容器」役
# 「容器」を入れることもできる
class Branch:
	def __init__(self, name):
		self.name = name
		self.list = []

	def add_leaf(self, leaf):
		self.list.append(leaf)

	def add_branch(self, branch):
		self.list.append(branch)

	def cut(self):
		for component in self.list:
			if type(component) == Leaf:
				component.cut()
			elif type(component) == Branch:
				component.cut()

		print('{}を切りました'.format(self.name))


leaf1 = Leaf('leaf1')
leaf2 = Leaf('leaf2')
leaf3 = Leaf('leaf3')
leaf4 = Leaf('leaf4')
branch1 = Branch('branch1')
branch2 = Branch('branch2')

branch1.add_leaf(leaf1)
branch1.add_branch(branch2)
branch1.add_leaf(leaf4)
branch2.add_leaf(leaf2)
branch2.add_leaf(leaf3)

branch1.cut()