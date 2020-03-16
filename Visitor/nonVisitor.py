# Visitorパターンを用いない場合
# 新しい処理を追加して機能を拡張しようとするたびに、
# その機能を追加したい各クラスにそれぞれメソッドを追加・修正する必要がある

class Home:
	def __init__(self):
		self.name = '家'

	def water_works(self):
		print('{}の水道工事をします'.format(self.name))

	def electrical_construction_work(self):
		print('{}の電気工事をします'.format(self.name))


class Company:
	def __init__(self):
		self.name = '会社'

	def water_works(self):
		print('{}の水道工事をします'.format(self.name))

	def electrical_construction_work(self):
		print('{}の電気工事をします'.format(self.name))



home = Home()
home.water_works()
home.electrical_construction_work()

company = Company()
company.water_works()
company.electrical_construction_work()