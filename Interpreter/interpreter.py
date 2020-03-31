# Interpreterパターン
# 何らかの形式で書かれたデータを解析・処理を行い、その結果に伴って何らかの処理を行う機能を提供する
# 1つの規則を1つのクラスで表しているため、規則の追加や修正が容易にできる
# ドメインに特化した実装をすることで高効率化が計れる

from abc import ABCMeta, abstractclassmethod


# 逆ポーランド記法用計算機
class RPNCalculator:
	def __init__(self):
		self.syntax_tree = []

	# 逆ポーランド記法の数式を解析し、構文木を作成するメソッド
	def __parse(self, formula):
		self.syntax_tree.clear()
		for string in formula.split(' '):
			if string is '+':
				self.syntax_tree.append(Plus())
			elif string is '-':
				self.syntax_tree.append(Minus())
			elif string is '*':
				self.syntax_tree.append(Asterisk())
			elif string is '/':
				self.syntax_tree.append(Slash())
			else:
				self.syntax_tree.append(Number(int(string)))

	def calculate(self, formula):
		self.__parse(formula)
		context = []
		for expression in self.syntax_tree:
			expression.interpret(context)
		return context.pop()


class Operator(metaclass=ABCMeta):
	@abstractclassmethod
	def interpret(self, context):
		pass


# '+'の解釈
class Plus(Operator):
	def interpret(self, context):
		context.append(context.pop() + context.pop())


# '-'の解釈
class Minus(Operator):
	def interpret(self, context):
		context.append(- context.pop() + context.pop())


# '*'の解釈
class Asterisk(Operator):
	def interpret(self, context):
		context.append(context.pop() * context.pop())


# '/'の解釈
class Slash(Operator):
	def interpret(self, context):
		context.append(1 / context.pop() * context.pop())


# '数字'の解釈
class Number(Operator):
	def __init__(self, number):
		self.number = number

	def interpret(self, context):
		context.append(self.number)


calculator = RPNCalculator()
print('逆ポーランド記法で数式を入力＞')
formula = input()
result = calculator.calculate(formula)
print(f' = {result}')
