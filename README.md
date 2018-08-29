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
