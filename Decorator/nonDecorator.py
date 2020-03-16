# Decoratorパターンを用いない場合
# 継承を利用した機能、振る舞いの追加を行う
# この方法だと、非常に固定的な実装になってしまう
# チャーシューをトッピングした塩ラーメンが欲しいときには、
# 塩ラーメンクラスを継承した新しいクラスが必要になる

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


# チャーシュー醤油ラーメンクラス
class RoastPorkToppingSoySauceRamen(SoySauceRamen):
	def get_name(self):
		return 'チャーシュー醤油ラーメン'


# 味玉味噌ラーメンクラス
class SeasonedEggToppingMisoRamen(MisoRamen):
	def get_name(self):
		return '味玉味噌ラーメン'


soy_sauce_ramen = RoastPorkToppingSoySauceRamen()
miso_ramen = SeasonedEggToppingMisoRamen()
salted_ramen = SaltedRamen()

print(soy_sauce_ramen.get_name())
print(miso_ramen.get_name())
print(salted_ramen.get_name())