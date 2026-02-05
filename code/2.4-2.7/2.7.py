#2.7
#图书库存管理系统
#功能很基础，只是为了突出封装继承多态的概念
#这里将内存当作临时数据库
from functools import wraps
from symtable import Function


#这里写一个异常处理的功能,因为本身是在内存操作数据，所以一般都是参数给的有问题
def test(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            print("参数输入有问题，请重试")
            print(e)
            return None
    return wrapper

#图书数据类型基类
class Book:
    def __init__(self, name, num, type, course):
        self._name = name
        self._num = num
        self._type = type
        self._course = course
        self._borrowed = 0

    @property
    def name(self):
        return self._name
    @property
    def num(self):
        return self._num
    @property
    def type(self):
        return self._type
    @property
    def course(self):
        return self._course
    @property
    def borrowed(self):
        return self._borrowed

    def info(self):
        pass

    def borrow_book(self):
        self._borrowed += 1
        self._num -= 1

    def return_book(self):
        self._borrowed -= 1
        self._num += 1

class FictionBook(Book):#科幻书籍
    def __init__(self, name, num):
        super().__init__(name, num, "Fiction", None)
    #这里可以新增科幻书籍的一些特性,或者方法达到多态的特性

    def info(self):
        print(f"书籍类型:{self.type}")
        print(f"书名: {self.name}")
        print(f"库存量: {self.num}")
        print(f"已借出{self.borrowed}")

class TextBook(Book):#教材
    def __init__(self, name, num, course):
        super().__init__(name,num, "TextBook", course)

    #这里就可以体现多态
    def info(self):
        print(f"书籍类型:{self.type}")
        print(f"教材科目:{self.course}")
        print(f"书名: {self.name}")
        print(f"库存量: {self.num}")
        print(f"已借出{self.borrowed}")

class Library:#图书馆控制类
    def __init__(self):
        self._books:list[Book] = []
        print(f"图书管理系统初始化，当前图书数量{len(self._books)}")

    @property
    def books(self):
        return self._books

    @test
    def add(self, book:Book):
        self._books.append(book)
        print("新书添加成功")
        book.info()

    @test
    def quire_with_name(self, name, type=None, course=None):
        for book in self._books:
            if book.name == name: book.info()

    @test
    def borrow_book(self,name:str,type=None,course=None):
        for book in self._books:
            if book.name == name:
                if book.type == type and book.course == course:
                    if book.num <= 0:
                        print("当前图书已被借完")
                    else:
                        print("借书成功")
                        book.borrow_book()
                        book.info()
                    return

    @test
    def return_book(self,name:str,type=None,course=None):
        for book in self._books:
            if book.type == type and book.course == course:
                if book.borrowed <= 0:
                    print("当前所还图书不属于该图书馆")
                else:
                    book.return_book()
                return


#这里只做小小的演示

#import ...
book1 = FictionBook("三体1",2)
book2 = FictionBook("三体2",2)
book3 = TextBook("高数",5,"数学")
Lib = Library()
Lib.add(book1)
Lib.add(book2)
Lib.add(book3)

Lib.quire_with_name(book2.name)#查询功能测试

for i in range(2):
    Lib.borrow_book(book1.name,book1.type, book1.course)
Lib.borrow_book(book1.name,book1.type, book1.course)#测试超借功能

for i in range(5):
    Lib.borrow_book(book3.name,book3.type,book3.course)
Lib.borrow_book(book3.name,book3.type,book3.course)#测试超借功能

for i in range(5):
    Lib.return_book(book3.name,book3.type, book3.course)
Lib.return_book(book3.name,book3.type, book3.course)#超还功能检测