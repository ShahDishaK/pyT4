import numpy as np

a=np.array([5,1,3,6,4])
b=np.sort(a)
a
b

a.sort()
a

b=np.random.randint(1,100,24).reshape(6,4)
print(b)
np.sort(b,axis=0)#1 for horizontal,0 for vertical

arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
new1=np.array_split(arr,3,axis=1)#devides in 3 arrays
new1

x=np.array([[1,2],[3,4]])
for i in x:
    print(i)
for i in np.nditer(x):
    print(i)

class PyProf:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("creator of python",self.name)
class JvaProg:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Creator of java",self.name)
p1=PyProf("Hitexa")
p1.show()
p2=JvaProg("Disha")
p2.show()

class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name,"is a teacher")
class Professor(Person):
    pass
p1=Professor("Rahul")
p1.show()

#heirachical inheritance
class Human(Person):
    pass
class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name,"is a teacher")
class Professor(Person):
    pass
p1=Professor("Rahul")
p2=Professor("Nidhi")
p2.show()
p1.show()

class Person:
    def __init__(self,name):
        self.name=name
    def p(self):
        print(self.name,"programmer")
class Java(Person):
    pass
class Python(Person):
    pass
p1=Java("java")
p1.p()
p2=Python("Python")
p2.p()

# multiple
class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name,"is a person")
class Teacher:
    def credit(self):
        print("she teches python")
        
class PythonProg(Person,Teacher):
    pass
p1=PythonProg("Disha")
p1.show()
p1.credit()

# multilevel
class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name,"is a person")
class Teacher(Person):
    pass
        
class PythonProg(Teacher):
    pass
p1=PythonProg("Disha")
p1.show()


# super
class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name,"is a person")
class Teacher(Person):
    def fun(self):
        print("from child")
        super().show()
        print("back to child")
a1=Teacher("Disha")
a1.fun()

