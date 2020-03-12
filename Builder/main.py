from builder import TeaBuilder, CoffeeBuilder, DrinkDirectorSweetened, DrinkDirectorSugarfree
from drinks import Tea, Coffee

# Builderパターンを用いた場合
# 作成したいオブジェクトのBuilderのインスタンスをDirectorに渡すことで、
# 期待するオブジェクトを作成させ、それを得ることができる
# 作成の方法や過程は意識する必要が無く、Builderを変えれば他のオブジェクトも得ることができる
print('================')
print('加糖ドリンク')
print('================')

tea_builder = TeaBuilder()
tea_director = DrinkDirectorSweetened(tea_builder)
tea_director.constract()
tea = tea_builder.get_result()
tea.drink()
print('----------------')
coffee_builder = CoffeeBuilder()
coffee_director = DrinkDirectorSweetened(coffee_builder)
coffee_director.constract()
coffee = coffee_builder.get_result()
coffee.drink()

print('================')
print('無糖ドリンク')
print('================')

tea_builder = TeaBuilder()
tea_director = DrinkDirectorSugarfree(tea_builder)
tea_director.constract()
tea = tea_builder.get_result()
tea.drink()
print('----------------')
coffee_builder = CoffeeBuilder()
coffee_director = DrinkDirectorSugarfree(coffee_builder)
coffee_director.constract()
coffee = coffee_builder.get_result()
coffee.drink()

# Builderパターンを用いない場合
# 期待するオブジェクトを作成するために必要な処理を全て利用側が呼び出して実行しなければならない
# 利用側に実装を隠蔽できないため依存が強くなる
print('================')
print('Builder無し')
print('================')

tea_builder = TeaBuilder()
tea_builder.prepare_cup()
tea_builder.add_sugar(10)
tea_builder.set_source_of_drink()
tea_builder.pour_hot_water(150)
tea = tea_builder.get_result()
tea.drink()
print('----------------')
coffee_builder = CoffeeBuilder()
coffee_builder.prepare_cup()
coffee_builder.add_sugar(30)
coffee_builder.set_source_of_drink()
coffee_builder.pour_hot_water(200)
coffee = coffee_builder.get_result()
coffee.drink()
