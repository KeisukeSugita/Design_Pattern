# Singletonパターン
# 複数のインスタンスの生成を認めず、
# インスタンスが一つしか存在しないことを保証する
# 外部からインスタンスを生成できない
# システムの中に1つしか存在しないものをプログラムで表現できる

class Identification(object):
    __instance = None

    def __new__(cls):
        raise NotImplementedError('インスタンスはget_instanceメソッドで取得してください')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = super(Identification, cls).__new__(cls)
            print(type(cls.__instance))
        return cls.__instance

    # 通常のインスタンス作成方法でシングルトンを実現
    '''
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(Identification, cls).__new__(cls)
        return cls.__instance
    '''


# インスタンスの生成
id1 = Identification.get_instance()
id1.name = '氏名'
id1.address = '住所'
print(id1.name)
print(id1.address)

# id1と同じインスタンスになる
id2 = Identification.get_instance()
print(id2.name)
print(id2.address)

# id3 = Identification() ←エラー


'''
id1 = Identification()
id1.name = '氏名'
id1.address = '住所'
print(id1.name)
print(id1.address)

id2 = Identification()
print(id2.name)
print(id2.address)
'''