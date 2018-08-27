#### 项目新建
* 添加 `.gitignore`

* 新建 python package
> Directory与Python package的区别:
> * Dictionary在pycharm中就是一个文件夹，放置资源文件，对应于在进行JavaWeb开发时用于放置css/js文件的目录，或者说在进行物体识别时，用来存储背景图像的文件夹
> * python package就是一个目录，其中包括一组模块和一个 `__init.py__` 文件

#### lambda表达式
> 相当于匿名函数

```map( lambda x: x*x, [y for y in range(10)] )```

#### 函数式编程
> * 不依赖于外部的数据，而且也不改变外部数据的值，而是返回一个新的值给你
> * 把函数当成变量来用，关注于描述问题而不是怎么实现
> * Python中的除了map和reduce外，还有一些别的如filter, find, all, any的函数做辅助，可以让代码更简洁易读
