#### 项目新建
* 添加 `.gitignore`

* 新建 python package
> Directory与Python package的区别:
> * Dictionary在pycharm中就是一个文件夹，放置资源文件，对应于在进行JavaWeb开发时用于放置css/js文件的目录，或者说在进行物体识别时，用来存储背景图像的文件夹
> * python package就是一个目录，其中包括一组模块和一个 `__init.py__` 文件

#### lambda表达式
> 相当于匿名函数

```map( lambda x: x*x, [y for y in range(10)] )```

```fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)```

#### 函数式编程
* 不依赖于外部的数据，而且也不改变外部数据的值，而是返回一个新的值给你
* 把函数当成变量来用，关注于描述问题而不是怎么实现
* Python中的除了 `map` 和 `reduce` 外，还有一些如 `filter`, `find`, `all`, `any`函数做辅助，可以让代码更简洁易读

#### 面向切面编程AOP和装饰器
* 装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等
* 有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用
* 装饰器的作用就是为已经存在的对象添加额外的功能

```
@f1(arg)
@f2
def func(): pass
```
is equivalent to:
```
def func(): pass
func = f1(arg)(f2(func))
```
* python中函数就是对象，可以赋值给一个变量，也可以在其他函数里定义
* 装饰器就是"wrappers", 它可以让你在你装饰函数之前或之后执行程序, 而不用修改函数本身
```
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs: --ham--

sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
```
相当于
```
@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
```
如果改变decorator的位置
```
@ingredients
@bread
def strange_sandwich(food="--ham--"):
    print(food)

strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~
```

#### Python的函数参数传递
* 不可变对象：int，string，float，tuple
```
>>> a='abcc'
>>> a.replace('c','k')
'abkk'
>>> a
'abcc'
```

```
a = 1
def fun(a):
    print(a)  # 1
    print(id(a))  # 4366880800
    a = 2
    print(id(a))   # 4366880832
print(id(a))  # 4366880800
fun(a)
print(a)  # 1
```
* 可变对象：list，dictionary, set
```
>>> list = [1, 2, 3]
>>> list2 = list
>>> list2.remove(1)
>>> list
[2, 3]
>>>
>>>a = [1]
>>>b = a
>>>b[0] = 2
>>>a
[2]
```

```
a = [1, 2, 3]

def fun(a):
    print(a)  # [1, 2, 3]
    print(id(a))  # 4499711048

    a.append(2)
    print(id(a))  # 4499711048

print(id(a))  # 4499711048
fun(a)
print(a)  # [1, 2, 3, 2]
```

###### Java传参
* 基本数据类型
> 包括：byte, short, int, long, char, float, double, Boolean, returnAddress
* 引用数据类型
> 包括：类类型，接口类型和数组
* 值类型
> 对象本身不允许修改，数值的修改实际上是让变量指向了一个新的内存地址
* 引用类型
> 对象本身可以修改

#### Python中的元类 ([metaclass](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python))
> ORM（对象关系映射）中比较常用

#### 实例方法、静态方法、类方法
```
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```
* 静态方法是指类中无需实例参与即可调用的方法(不需要self参数)，直接在类之后使用`.`号运算符调用方法
> 与类里面的其他属性，方法没有关系
```
class ClassA(object):

    @staticmethod
    def func_a():
        print('Hello Python')

if __name__ == '__main__':

    # 直接调用
    ClassA.func_a()
```
* 类方法传入的第一个参数为cls，是类本身。并且，类方法可以通过类直接调用，或通过实例直接调用。但无论哪种调用方式，最左侧传入的参数一定是类本身
```
class ClassA(object):

    @classmethod
    def func_a(cls):
        print(type(cls), cls)


if __name__ == '__main__':

    # 直接调用
    ClassA.func_a()

    # 通过实例调用
    ca = ClassA()
    ca.func_a()
```
* 实例方法需要将类实例化后调用，如果使用类直接调用实例方法,需要显式地将实例作为参数传入
```
class ClassA(object):

    def func_a(self):
        print('Hello Python')

if __name__ == '__main__':

    # 使用实例调用实例方法
    ca = ClassA()
    ca.func_a()

    # 如果使用类直接调用实例方法,需要显式地将实例作为参数传入
    ClassA.func_a(ca)
```

#### 类变量和实例变量
* 类变量是可在类的所有实例之间共享的值，它们不是单独分配给每个实例的
* 实例变量是实例化之后，每个实例单独拥有的变量
```
class Test(object):
    # 类变量
    num = 0

    def __init__(self, name):
        self.name = name
        Test.num += 1


if __name__ == '__main__':
    print(Test.num)  # 0
    t1 = Test('jas')
    print(Test.num)  # 1
    t2 = Test('fortunate')
    print(Test.num)  # 2

    # 在实例的作用域里把类变量的引用改变了, 就变成了一个实例变量, 所以 t1.num 和 t2.num 输出2
    print(t1.name, t1.num)  # jas 2
    print(t2.name, t2.num)  # fortunate 2
```

```
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa
```
对比
```
class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print(p1.name)  # [1]
print(p2.name)  # [1]
print(Person.name)  # [1]
```

#### Python自省
> 自省就是用面向对象的语言写的程序在运行时, 就能知道对象的类型

#### 字典推导式
`d = {key: value for (key, value) in iterable}`
```
@字典推导式
#city_rate.txt 存储数据如下
110000  0.88
120000  0.65
130100  0.65
130200  0.65
130300  0.65

#将文件中的数据转换成字典（键值对）方法
#这个方法在python3中可用，在python2.7中用不了会出错
code_to_rate = {k:v for k,v in [line.strip().split('\t') for line in open("city_rate.txt").readlines()]}

# 输出
{'110000': '0.88', '120000': '0.65', '130100': '0.65', '130200': '0.65', '130300': '0.65'}
```

#### Python中单下划线和双下划线
* 以单下划线开头 `_private` ，表示这是一个保护成员，只有类对象和子类对象自己能访问到这些变量。以单下划线开头的变量和函数被默认当作是内部函数
* 双下划线开头 `__private` ，表示为私有成员，只允许类本身访问，子类也不行
* 以单下划线结尾 `private_` , 仅仅是为了区别该名称与关键词
* 双下划线开头，双下划线结尾 `__private__` 是一种约定，表示Python内部的名字，用来区别其他用户自定义的命名,以防冲突
```
class Myclass():
    def __init__(self):
        self.__superprivate = 'hello'
        self._semiprivate = ',world'


mc = Myclass()
print(mc.__superprivate)
# AttributeError: 'Myclass' object has no attribute '__superprivate'

print(mc._semiprivate)
# ,world

print(mc.__dict__)
# {'_Myclass__superprivate': 'hello', '_semiprivate': ',world'}
```

#### 字符串格式化: %和 .format
.format 更加实用
```
sub1 = 'hi'
a = '{}, jasmine'.format(sub1)
print(a)    # hi, jasmine
```

#### 迭代器和生成器
###### 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。比如我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器 Generator：边循环，边计算
* Iterables
```
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
```
> These iterables are handy because you can read them as much as you wish, but you store all the values in memory and this is not always what you want when you have a lot of values
* Generators
```
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```
> Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:
It is just the same except you used `( )` instead of `[ ]`. BUT, you cannot perform for i in mygenerator a second time since generators can only be used once
* Yield
```
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```
> * yield is a keyword that is used like return, except the function will return a generator
> * The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.
The generator is considered empty once the function runs, but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore
> * yield返回执行结果并不中断程序执行，return在返回执行结果的同时中断程序执行

#### `*args` and `**kwargs`
* `*args` 可以传递任意数量的参数
```
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print '{0}. {1}'.format(count, thing)
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage
```
* `**kwargs` 允许你使用没有事先定义的参数名
```
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print '{0} = {1}'.format(name, value)
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit
```
* `*args` 和 `**kwargs` 可以同时在函数的定义中,但是 `*args` 必须在 `**kwargs` 前面
* 调用函数时也可以用 `*` 和 `**` 语法
```
>>> def print_three_things(a, b, c):
...     print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))
...
>>> mylist = ['aardvark', 'baboon', 'cat']
>>> print_three_things(*mylist)
a = aardvark, b = baboon, c = cat
```

#### 鸭子类型 Duck typing
```
class Duck:
    def quack(self):
        print("Quaaaaaack!")


class Bird:
    def quack(self):
        print("bird imitate duck.")


class Dog:
    def quack(self):
        print("dog imitate duck.")


def in_the_forest(duck):
    duck.quack()


duck = Duck()
bird = Bird()
dog = Dog()

for x in [duck, bird, dog]:
    in_the_forest(x)

#  输出
# Quaaaaaack!
# bird imitate duck.
# dog imitate duck.
```
> `bird` 和`dog` 类拥有和 `duck` 类一样的方法，当有一个函数调用 `duck` 类，并利用到了 `quack()` 方法，我们传入 `bird` 和 `dog` 类一样可以运行，函数并不会检查对象的类型是不是 `duck`，只用它拥有 `quack()`方法，就可以正常的被调用

#### Python中无需函数重载

#### old-style and new-style classes
> No matter if you subclass from object or not, classes are new-style in Python 3

#### `__new__` 和 `__init__` 的区别
* Use `__new__` when you need to control the creation of a new instance. Use `__init__` when you need to control initialization of a new instance
* `__new__` is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, `__init__` doesn't return anything; it's only responsible for initializing the instance after it's been created
* `__new__` is static class method, while `__init__` is instance method.  `__new__` has to create the instance first, so `__init__` can initialize it. Note that `__init__` takes `self` as parameter. Until you create instance there is no `self`
* `__new__()` 在 `__init__()` 之前被调用，用于生成实例对象
> 可以分别使用 `__metaclass__` , `__new__` 和 `__init__` 来分别在类创建,实例创建和实例初始化
```
class A(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print("EXISTS")
            return A._dict['key']
        else:
            print("NEW")
            return super(A, cls).__new__(cls)

    def __init__(self):
        print("INIT")
        A._dict['key'] = self
        print("")

a1 = A()
a2 = A()
a3 = A()

#  输出
NEW
INIT

EXISTS
INIT

EXISTS
INIT
```

#### 单例模式
主要目的是确保某一个类只有一个实例存在
> Python 的模块是天然的单例模式，在大部分情况下是够用的
* 使用模块
```
# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()
```
```
# to use
from mysingleton import my_singleton

my_singleton.foo()
```
* 使用 `__new__`
```
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1
```
```>>> one = MyClass()
>>> two = MyClass()
>>> one == two
True
>>> one is two
True
>>> id(one), id(two)
(4303862608, 4303862608)
```
* 使用装饰器
```
from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
```
```
@singleton
class MyClass(object):
    a = 1
```
* 使用元类 metaclass
```
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python2
class MyClass(object):
    __metaclass__ = Singleton

# Python3
# class MyClass(metaclass=Singleton):
#    pass
```

#### Python中的作用域
当 Python 遇到一个变量, 会按照这样的顺序进行搜索：本地作用域（Local）→ 当前作用域被嵌入的本地作用域（Enclosing locals）→ 全局/模块作用域（Global）→ 内置作用域（Built-in）

#### GIL（Global Interpreter Lock）线程全局锁
* Python为了保证线程安全而采取的独立线程运行的限制，就是一个核只能在同一时间运行一个线程
* 对于io密集型任务，python的多线程起到作用，但对于cpu密集型任务，python的多线程几乎占不到任何优势，还有可能因为争夺资源而变慢

#### 协程
协程是进程和线程的升级版, 进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间, 而协程就是用户自己控制切换的时机, 不再需要陷入系统的内核态
> Python里最常见的yield就是协程的思想

