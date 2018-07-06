#类同样是对象， 只要使用class ，python解释器在执行时就会创建对象，如：
class ObjectCreator:    
    pass
print(ObjectCreator.__dict__)

#元类是创建类的类，可以这样理解：
MyClass = MetaClass()
MyObject = MyClass()
#https://www.cnblogs.com/tkqasn/p/6524879.html