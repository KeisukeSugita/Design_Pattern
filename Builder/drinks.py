from abc import ABCMeta, abstractclassmethod

# DrinkBuilderで作成するオブジェクトを定義するインターフェース
class Drink(metaclass=ABCMeta):
    __sugar = 0
    __hot_water = 0
    @abstractclassmethod
    def drink(self):
        pass


# 紅茶
class Tea(Drink):
    def drink(self):
        print('紅茶を飲みました')


# コーヒー
class Coffee(Drink):
    def drink(self):
        print('コーヒーを飲みました')