class ObjectDict:    
    def __getattr__(self,name):
        print(name)
        #super(ObjectDict).__getattr__(self)
        return name
    #
    def __getattribute__(self,attr):
        print('__getattribute__ {}'.format(attr))
        return object.__getattribute__(self,attr)
        #return super().__getattribute__(attr) 可以运行 super参数不用传递self
if __name__ == '__main__':
    o = ObjectDict()
    o.a = 1
    #__getattr__当调用属性报错时，执行的函数
    print(o.a)#a
    print(o.b)#b
