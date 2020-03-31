# Flyweightパターン
# 同じインスタンスを共有することで、メモリの使用量を減らす目的
# 複数スレッドからでも2度作成されないようにすることに注意する必要がある場合もある


# BigNumberを作成するクラス　同じBigNumberのインスタンスは作成しない
# Singleton
class BigNumberFactory:
    __instance = None
    __big_numbers = {}

    def __new__(cls):
        raise NotImplementedError('インスタンスはget_instanceメソッドで取得してください')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = super(BigNumberFactory, cls).__new__(cls)
            print(type(cls.__instance))
        return cls

    def get_big_number(self, number):
        if number in self.__big_numbers:
            big_number = self.__big_numbers[number]
        else:
            big_number = BigNumber(number)
            self.__big_numbers[number] = big_number
        return big_number


class BigNumber:
    def __init__(self, number):
        self.number_data = ''
        file = open(f'{number}.txt', 'r')
        for row in file:
            self.number_data += row
        file.close()


big_number_factory = BigNumberFactory.get_instance()
print('input numbers', end='>')
to_big_numbers = input()
for to_big_number in to_big_numbers:
    big_number = big_number_factory.get_big_number(big_number_factory, to_big_number)
    print(big_number.number_data)
