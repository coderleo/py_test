class cls:
    _instance = None
    def __new__(cls,*args,**kwargs):
        
        if cls._instance is None:
            print(111)
            cls._instance =  super().__new__(cls)
        return cls._instance
    
    def __init__(self,status):
        self.status = status
    

c1 = cls(1)
c2 = cls(2)
print(c1==c2)
print(c1.status)
print(c1.__class__)#类似于type()

