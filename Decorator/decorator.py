# Decoratorパターン
# オブジェクトに新しい機能や振る舞いを動的に追加することができる
# 追加したい機能や振る舞いに、もとのオブジェクトと同じインターフェースを持たせることで、
# より柔軟な機能拡張が可能になる

from abc import ABCMeta, abstractclassmethod


# ラーメンインターフェース
class Ramen(metaclass=ABCMeta):
	@abstractclassmethod
	def get_name(self):
		pass


# 醤油ラーメンクラス
class SoySauceRamen(Ramen):
	def get_name(self):
		return '醤油ラーメン'


# 味噌ラーメンクラス
class MisoRamen(Ramen):
	def get_name(self):
		return '味噌ラーメン'


# 塩ラーメンクラス
class SaltedRamen(Ramen):
	def get_name(self):
		return '塩ラーメン'


# チャーシュートッピングラーメンクラス
class RoastPorkToppingRamen(Ramen):
	def __init__(self, ramen):
		self.__ramen = ramen

	def get_name(self):
		return 'チャーシュー{}'.format(self.__ramen.get_name())


# 味玉トッピングラーメンクラス
class SeasonedEggToppingRamen(Ramen):
	def __init__(self, ramen):
		self.__ramen = ramen

	def get_name(self):
		return f'味玉{self.__ramen.get_name()}'


soy_sauce_ramen = RoastPorkToppingRamen(SoySauceRamen())
miso_ramen = SeasonedEggToppingRamen(MisoRamen())
salted_ramen = SeasonedEggToppingRamen(RoastPorkToppingRamen(SaltedRamen()))

print(soy_sauce_ramen.get_name())
print(miso_ramen.get_name())
print(salted_ramen.get_name())