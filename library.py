"""
抽象出来三个对象
读者 1读者列表 2查询 3借书 4还书
图书馆 1书籍列表 2查询 3借书 4还书
图书馆系统 对读者和图书进行管理
"""

# import os
import json

"""
book_dict = {'book_a': ['author_a'], 'book_b': ['author_b'], 'book_c': ['author_c'],
             'book_d': ['author_d'], 'book_e': ['author_e']}
reader_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
os.mknod('read_dict.json')
f = open('read_dict.json', 'w')
# writeline 后边是一个序列，会迭代的帮你输入
f.writelines(json.dumps(reader_dict)+'\n')
# book_dict = json.load(f)
f.close()
os.mknod('book_dict.json')
g = open('book_dict', 'w')
g.writelines(json.dumps(book_dict)+'\n')
g.close
"""

f = open('book_dict.json', 'r')
book_dict = json.load(f)
f.close()

g = open('reader_dict', 'r')
reader_dict = json.load(g)
g.close()


def inquire():
    reader = input('please inter your name:')
    if reader in reader_dict:
        if reader_dict[reader] < 3:
            book = input('please inter book name')
            if book in book_dict:
                if len(book_dict[book]) == 1:
                    book_dict[book].append(reader)
                    reader_dict[reader] = reader_dict[reader] + 1
                else:
                    book_dict[book].append(reader)
                    print('reading, booking for you')
            else:
                print('there is no this book')
        else:
            print('too many books you rend')
    else:
        print('you are not the reader')
    return '这个应该写什么内容啊'


def manage():
    manager = input('please inter your name')
    if manager == 'boss':
        pass
        # this way is easy to make it


a = inquire()
print(reader_dict)
print(book_dict)
f = open('book_dict.json', 'w')
f.writelines(json.dumps(book_dict)+'\n')
f.close()
f = open('reader_dict.json', 'w')
f.writelines(json.dumps(reader_dict)+'\n')
f.close()



