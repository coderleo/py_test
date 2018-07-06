class cls:
    clsvar = 1
    def __init__(self):
        self.insvar = 2
    def show(self):
        print('show')
ins1 = cls()
ins2 = cls()
print(cls.__dict__)
# {'__module__': '__main__', 'clsvar': 1, '__init__': <function cls.__init__ at 0x02B346A8>, 'show': <function cls.show at 0x02B34618>, 
# '__dict__': <attribute '__dict__' of 'cls' objects>, '__weakref__': <attribute '__weakref__' of 'cls' objects>, '__doc__': None}
print(ins1.__dict__)
#{'insvar': 2}
#根据上面可以看到 show函数并没有出现在对象的__dict__中
#__dict__存储的是当前对象的所有属性，注意：def(self)不算对象方法，而算类方法
#一个对象的属性查找顺序遵循首先查找实例对象自己，然后是类，接着是类的父类

