# Commandパターンを利用しない場合
# 利用者がReceiverの内容を全て知っている必要がある
# 実行した処理の履歴管理が難しい


# Receiver
class Television:
	def plug_in(self):
		print('コンセントを差し込みます')

	def unplug(self):
		print('コンセントを抜きます')

	def push_power_button(self):
		print('電源ボタンを押します')

	def turn_on(self):
		print('電源がONになりました')

	def turn_off(self):
		print('電源がOFFになりました')

	def record(self):
		print('録画しました')

	def delete_record_data(self):
		print('録画を削除しました')


television = Television()

television.plug_in()
television.push_power_button()
television.turn_on()
television.record()
television.push_power_button()
television.turn_off()
television.unplug()
television.plug_in()
television.push_power_button()
television.turn_on()
television.delete_record_data()
television.record()
television.push_power_button()
television.turn_off()
television.unplug()
