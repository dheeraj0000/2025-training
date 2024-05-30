class A:
    n=10
    def __init__(self,z,y=5):
        self.zee=z
        self.yes=y
    def disp(self):
        print(self.zee,self.n)
class B(A):
    def __init__(self,m,x,p):
        self.my=m
        A.__init__(self,x,p)
obj=B(10,15,21)
obj.disp()