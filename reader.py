# build a reader class


class Book(object):
    def __init__(self, title, author, borrower='', waiters=[]):
        self.title = title
        self.author = author
        self.borrower = borrower
        self.waiters = waiters

    def info(self):
        return self.title, self.author

    def search(self):
        return self.borrower
        return self.waiters


class Reader(object):
    # name='' 可以直接输入字符串//init缺少一个- 引发的惨案
    def __init__(self, name, borrow_books=[]):
        self.name = name
        self.borrow_books = borrow_books

    def borrow(self,  title='', borrow_books=[], flag=1):
        if flag == 1:
            if len(borrow_books) < 4:
                borrow_books.append(title)
            else:
                print('too many books you borrow')
        else:
            borrow_books.remove(title)


class Library(object):
    # for book
    def add_book(self, books=[], book=Book()):
        books.append(book.title)
        return books

    def delete_book(self, books, book=Book()):
        books.remove(book.title)
        return books

    def find_book(self, books, book=Book()):
        return books.index(book.title)

    # for reader
    def add_reader(self, readers=[], reader=Reader()):
        readers.append(reader.name)
        return reader

    def delete_reader(self, readers, reader=Reader()):
        readers.remove(reader.name)
        return readers

    def find_reader(self, readers, reader=Reader()):
        return readers.index(reader.name)

    def borrow_book(self, reader=Reader(), book=Book()):
        books.remove(book.title)
        reader.borrow(reader.name, book.title, 0)
        return books, reader.borrow

    def return_book(self, reader=Reader(), book=Book()):
        books.append(book.title)
        reader.borrow(reader.name, book.title, 1)


# test
if __name__ == '__main__':
    library = Library()
    books = []  # 图书馆的书
    readers = []  # 图书馆的读者
    # 创建四个书实例
    book1 = Book('Gone with wind', 'a')
    book2 = Book('Just do it', 'b')
    book3 = Book('You are right', 'c')
    book4 = Book('come on', 'd')
    # 创建5个读者实例
    reader1 = Reader('tony')
    reader2 = Reader('jack')
    reader3 = Reader('tom')

    # 图书的相关测试
    library.add_book(books, book1)
    library.add_book(books, book2)
    library.add_book(books, book3)
    library.add_book(books, book4)
    print('add book test:', books)
    library.delete_book(books, book4)
    print('delete book test:', books)
    library.find_book(books, book1)
    print('find book test')
    # 读者的相关测试
    library.add_reader(readers, reader1)
    library.add_reader(readers, reader2)
    library.add_reader(readers, reader3)
    print('add readers test:', readers)
    library.delete_reader(readers, reader3)
    print('delete reader test:', readers)
    library.find_reader(readers, reader1)
    print('find reader test:', reader1)
    # 借阅图书
    library.borrow_book(reader1, book1)
    print('borrow test', books, reader1.borrow_books)
    # 归还图书
    library.return_book(reader1, book1)
    print('return book test:', books, reader1.borrow_books)
















