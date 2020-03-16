# Strategyパターン
# 分岐が生じるアルゴリズム毎にクラスを作成し、
# それらに共通のインターフェースを持たせることで見通しが良くなる
# アルゴリズムの追加や変更が容易になり、メンテナンスもしやすくなる

from abc import ABCMeta, abstractclassmethod


class Fighter:
	def __init__(self, max_hp, strategy):
		self.__max_hp = max_hp
		self.hp = max_hp
		self.__strategy = strategy

	def act(self):
		self.__strategy.act(self)


class Strategy(metaclass=ABCMeta):
	@abstractclassmethod
	def act(self, fighter):
		pass


class AttackStrategy(Strategy):
	def act(self, fighter):
		print('攻撃します')


class DefenseStrategy(Strategy):
	def act(self, fighter):
		if fighter.hp < fighter._Fighter__max_hp:
			print('防御します')
		else:
			print('攻撃します')


class RecoveryStrategy(Strategy):
	def act(self, fighter):
		if fighter.hp < (fighter._Fighter__max_hp / 2):
			print('回復します')
		elif fighter.hp < fighter._Fighter__max_hp:
			print('防御します')
		else:
			print('攻撃します')


fighter = Fighter(10, AttackStrategy())
fighter.act()
fighter.hp = 7
fighter.act()
fighter.hp = 4
fighter.act()
print('----------------')

fighter = Fighter(10, DefenseStrategy())
fighter.act()
fighter.hp = 7
fighter.act()
fighter.hp = 4
fighter.act()
print('----------------')

fighter = Fighter(10, RecoveryStrategy())
fighter.act()
fighter.hp = 7
fighter.act()
fighter.hp = 4
fighter.act()
print('----------------')