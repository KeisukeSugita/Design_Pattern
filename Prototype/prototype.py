# Prototypeパターン
# ひな形となるインスタンスから全く同じインスタンスを生成する
# 同じインスタンスが必要な時に、登録しておいたインスタンスのクローンを利用すれば管理がしやすい

from abc import ABCMeta, abstractmethod


# クローンを作るメソッドをもつインターフェース
class Cloneable(metaclass=ABCMeta):
    @abstractmethod
    def create_clone(self):
        pass


# 書籍クラス
# タイトル、著者、発行年を持つ
class Book(Cloneable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # 全く同じメンバを持つインスタンスを生成する
    def create_clone(self):
        return Book(self.title, self.author, self.year)


# 書籍のカタログ
class BookCatalog:
    catalog = {}

    def add_catalog(self, book):
        self.catalog[book.title] = book

    # カタログ内の書籍を、タイトルから生成する
    def create(self, title):
        return self.catalog[title].create_clone()


# 本棚クラス
# それぞれの本に蔵書番号をつけて管理している
class Bookshelf:
    books = {}

    def add_book(self, collection_number, book):
        self.books[collection_number] = book



book_catalog = BookCatalog()
book_a = Book('title_A', 'author_A', 'year_A')
book_b = Book('title_B', 'author_B', 'year_B')
book_catalog.add_catalog(book_a)
book_catalog.add_catalog(book_b)

bookshelf = Bookshelf()

bookshelf.add_book('0001', book_catalog.create('title_A'))
bookshelf.add_book('0002', book_catalog.create('title_B'))
bookshelf.add_book('0003', book_catalog.create('title_A'))

print(bookshelf.books['0001'].author)
print(bookshelf.books['0002'].author)
print(bookshelf.books['0003'].author)


'''
ShallowCopy
コピー元のオブジェクトとコピー先のオブジェクトがメモリ上の同じデータを参照している
側だけ別の入れ物を用意し、中身の参照は同じ

DeepCopy
オブジェクトとメモリ上のデータの両方をコピーする
コピー元とコピー先で別のメモリ上のデータを参照している
'''