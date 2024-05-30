class A:
    def __init__(self,z):
        self.zee=z
        
class B(A):
    def __init__(self,z,x):
        super().__init__(x)
        self.zee=z
    def p(self):
        print(self.zee,super().zee)
obj=B(10,15)
obj.p()