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
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper

def sandwich(food="--ham--"):
    print food

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
    print food

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
    print food

strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~
```