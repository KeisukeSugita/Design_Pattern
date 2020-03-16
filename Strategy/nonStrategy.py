# Strategyパターンを用いない場合
# if文によってアルゴルズムの変更を行っているため、
# 煩雑で見通しが悪いコードになっている

from abc import ABCMeta, abstractclassmethod


ATTACK_STRATEGY = 1
DEFENSE_STRATEGY = 2
RECOVERY_STRATEGY = 3


class Fighter:
	def __init__(self, max_hp, strategy):
		self.__max_hp = max_hp
		self.hp = max_hp
		self.__strategy = strategy

	def act(self):
		# このif文でアルゴリズムの選択を行っている
		# 分岐するアルゴリズムの種類が増えていくことを考えると、
		# 見通しが悪く、メンテナンスがしずらくなってしまう
		if self.__strategy == ATTACK_STRATEGY:
			print('攻撃します')

		elif self.__strategy == DEFENSE_STRATEGY:
			if self.hp < self._Fighter__max_hp:
				print('防御します')
			else:
				print('攻撃します')

		elif self.__strategy == RECOVERY_STRATEGY:
			if self.hp < (self.__max_hp / 2):
				print('回復します')
			elif self.hp < self.__max_hp:
				print('防御します')
			else:
				print('攻撃します')


fighter = Fighter(10, ATTACK_STRATEGY)
fighter.act()
fighter.hp = 7
fighter.act()
fighter.hp = 4
fighter.act()
print('----------------')

fighter = Fighter(10, DEFENSE_STRATEGY)
fighter.act()
fighter.hp = 7
fighter.act()
fighter.hp = 4
fighter.act()
print('----------------')

fighter = Fighter(10, RECOVERY_STRATEGY)
fighter.act()
fighter.hp = 7
fighter.act()
fighter.hp = 4
fighter.act()
print('----------------')