https://github.com/bpbpublications/Python-for-Cybersecurity-Cookbook
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



# abstrac class:This class is derived from abc import ABC,abstractmethod
# ABC IS A META CLASS WHICH DEfines behaviour of other class.
# abstract method of an abstract class must be defined in the child class.it is used when commmon 
# features are shared by all objects as they are.
from abc import ABC,abstractmethod
class Defence(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print("GUN is AK 47")
class Army(Defence):
    def area(self):
        print("Area is land")
class Navy(Defence):
    def area(self):
        print("Area is Sea")
a=Army()
b=Navy()
a.area()
a.gun()
b.area()
b.gun()

# method resolution order:(c3 linearized algorithm)
class A:
    def which(self):
        print("I am From A")
class B(A):
    def which(self):
        print("I am From B")
class C(A):
    def which(self):
        print("I am From C")
class D(B,C):
    def which(self):
        print("I an From D")
        super().which()
d=D()
d.which()

D.mro()

class F:
    pass
class E:
    pass
class D:
    pass
class C(D,F):
    pass
class B(D,E):
    pass
class A(B,C):
    pass

class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
class X(C,D):
    pass
# TypeError                                 Traceback (most recent call last)
# <ipython-input-2-e6066b25c528> in <module>
#       7 class D(B,A):
#       8     pass
# ----> 9 class X(C,D):
#      10     pass

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B

# DUNDER/SPECIAL/MEGIC METHOD
class Book:
    def __init__(self,title,author,pages):
        print("A book created")
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"A {self.title} book by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("Book destroyed")

b=Book("Harry Potter","JK Rowlin",500)#A book created

print(b)#A Harry Potter book byJK Rowlin

len(b)#500

del(b)#Book destroyed

print(b)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-6-67e500defa1b> in <module>
# ----> 1 print(b)

# NameError: name 'b' is not defined

__mul__
__init__
__it__
__str__
__gt__
__del__
__len__
__eq__
__next__
__call__
__get.items__
__add__