# 9-marker
# implement a python class hearichy for hendaling fractions.
# 1)Define an abstract base class FractionBase with 3 methods i)__add__ ii)simplify iii)__str__
# as abstract methods.
# 2)implement a concreate class fraction which inherits from FractionBase.
# 3)str method of fraction should return the string represantation of fraction
# 4)simplyfy method should reduce the fraction
# 5)Add method should add to fractions.
# 2/4=1/2(simplify)

from abc import ABC,abstractmethod
class FractionBase(ABC):
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def simplify(self):
        pass
    @abstractmethod
    def __add__(self,a2,b2):
        pass
class Fraction(FractionBase):
    def __init__(self,a1,b1):
        self.a1=a1
        self.b1=b1
    def __add__(self,a2):
         for i in range(1,self.b1+1):
            if self.b1%i==0 and a2.b1%i==0:
                gcd=i
         lcm1=(self.b1*a2.b1)//gcd
         new_b1=lcm1//self.b1
         new_b2=lcm1//a2.b1
         new_a1=self.a1*new_b1
         new_a2=a2.a1*new_b2
         sum=new_a1+new_a2
         return f"{sum}/{lcm1}"
    def __str__(self):
        return f"Given Value is {self.a1}/{self.b1}"
    def simplify(self):
        for i in range(1,self.a1+1):
            if self.a1%i==0 and self.b1%i==0:
                gcd=i
#         np.gcd(self.a1,self.b1)
        self.a1=self.a1/gcd
        self.b1=self.b1/gcd
f1=Fraction(2,8)
f2=Fraction(2,8)
print(f1+f2)
print(f1)
print(f1)
f1.simplify()
print(f1)

import numpy as np

# implement py class money to handle monetory values in rupees and paisa class should provide functionalities like add,comparision,subtraction and claculation of total amount based on quantity.
# write nacessary method like __Add__ ,__sub__,__ge__,__str__,calculateTotal(self,quantity),priceForItem(self,total,quantity)

class nomenyException(Exception):
    def __init__(self,msg):
        self.msg=msg
class Money:
    def __init__(self,rs,pai):
        self.rs=rs
        self.pai=pai
    def __add__(self,other):
        totalpai=self.pai+other.pai
        totalrs=0
        while totalpai>=100:
            totalrs+=1
            totalpai-=100
        sum=self.rs+other.rs+totalrs
        return f"{sum}rs  {totalpai} paisa"
    def __sub__(self,other):
        subtractionrs=self.rs-other.rs
        subtractionpai=self.pai-other.pai
        try:
            if subtractionrs<0:
                raise nomenyException("no enought money")
            else:
                return f"{subtractionrs}rs {subtractionpai}paisa"
        except nomenyException as e:
            print(e)
    def __ge__(self,other):
        if self.rs>other.rs:
            return f"{self.rs} is greater"
        else:
            return f"{other.rs} is greater"
    def __str__(self):
        return f"{self.rs}rs and {self.pai}paisa"
    def calculateTotal(self,quantity,price):
        totalPrice=price*quantity
        return totalPrice
    def priceForItem(self,total,quantity):
        for1=total/quantity
        return for1
        
m1=Money(100,50)
m2=Money(20,50)
print(m2-m1)
            
        