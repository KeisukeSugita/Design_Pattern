# Builderパターン
# DirectorはBuilderのメソッドを使ってオブジェクトを生成し、
# 利用側にはその構築過程を隠蔽できる
# 利用側は作成したいオブジェクトのBuilderをDirectorに渡すだけで、
# 期待するオブジェクトを取得することができる
# インスタンスを作成することが目的(前提)
# constractの処理内容によって作成されるインスタンスを変えることができる

from abc import ABCMeta, abstractclassmethod
from drinks import Tea, Coffee


# Builderクラス
# 飲み物を作成する過程を定義している
class DrinkBuilder(metaclass=ABCMeta):
    # カップを用意する
    @abstractclassmethod
    def prepare_cup(self):
        pass

    # 砂糖を入れる
    @abstractclassmethod
    def add_sugar(self, sugar):
        pass

    # 飲み物の素をカップに入れる
    @abstractclassmethod
    def set_source_of_drink(self):
        pass

    # お湯を注ぐ
    @abstractclassmethod
    def pour_hot_water(self, hot_water):
        pass

    # 完成した飲み物を返す
    @abstractclassmethod
    def get_result(self):
        pass


# Directorクラス
# initで受け取ったBuilderのメソッドを呼び出し、オブジェクトを作成する
class DrinkDirectorSweetened:
    def __init__(self, builder):
        self.__builder = builder

    # Builderで作成したいオブジェクトを作成するためのメソッドを呼び出す
    # 利用側はこのメソッドを呼び出すだけで期待するオブジェクトを作成することができる
    def constract(self):
        self.__builder.prepare_cup()
        self.__builder.add_sugar(10)
        self.__builder.set_source_of_drink()
        self.__builder.pour_hot_water(150)


class DrinkDirectorSugarfree:
    def __init__(self, builder):
        self.__builder = builder

    # Builderで作成したいオブジェクトを作成するためのメソッドを呼び出す
    # 利用側はこのメソッドを呼び出すだけで期待するオブジェクトを作成することができる
    def constract(self):
        self.__builder.prepare_cup()
        self.__builder.add_sugar(0)
        self.__builder.set_source_of_drink()
        self.__builder.pour_hot_water(150)


class TeaBuilder(DrinkBuilder):
    def __init__(self):
        self.__tea = Tea()

    def prepare_cup(self):
        print('ティーカップを用意します')

    def add_sugar(self, sugar):
        print('砂糖を{0}g入れます'.format(sugar))
        self._TeaBuilder__tea._Drink__sugar += sugar

    def set_source_of_drink(self):
        print('ティーバッグを入れます')

    def pour_hot_water(self, hot_water):
        print('お湯を{0}ml入れます'.format(hot_water))
        self._TeaBuilder__tea._Drink__hot_water += hot_water

    def get_result(self):
        return self.__tea


class CoffeeBuilder(DrinkBuilder):
    def __init__(self):
        self.__coffee = Coffee()

    def prepare_cup(self):
        print('コーヒーカップを用意します')

    def add_sugar(self, sugar):
        print('砂糖を{0}g入れます'.format(sugar))
        self._CoffeeBuilder__coffee._Drink__sugar += sugar

    def set_source_of_drink(self):
        print('ドリップバッグを取り付けます')

    def pour_hot_water(self, hot_water):
        print('お湯を{0}ml入れます'.format(hot_water))
        self._CoffeeBuilder__coffee._Drink__hot_water += hot_water

    def get_result(self):
        return self.__coffee
