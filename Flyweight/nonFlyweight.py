# Flyweightパターンを利用しない場合
# 全く同じインスタンスを作成しているため、無駄なメモリを使用してしまう


class BigNumber:
    def __init__(self, number):
        self.number_data = ''
        file = open(f'{number}.txt', 'r')
        for row in file:
            self.number_data += row
        file.close()


print('input numbers', end='>')
to_big_numbers = input()
for to_big_number in to_big_numbers:
    big_number = BigNumber(to_big_number)
    print(big_number.number_data)
