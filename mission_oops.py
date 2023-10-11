# class Calculator:
#     def add(self,x,y):
#         print(x+y)
#     def sub(self,x,y):
#         print(x-y)
# cal= Calculator()
# cal.add(10,20)
# cal.sub(10,20)
# encapsulation-----------------------
# class Patient:
#     def __init__(self,pno,pname,page):
#         # print("pno is",pno)
#         print("pname is", pname)
#         print("page is", page)
#     def display(self,place):
#         print("place is",place)
# s2= Patient(14,"mukul",23)
# s2.display("bangalore")
# class School:
#     def __init__(self, name,age):
#         self.sname=name
#         self.sage=age
#     def display(self):
#         print(self.sname)
#         print(self.sage)
# s=School("nitish",23)
# s.display()#########################inside the class
# print(s.sname)########################## outside the class
# print(s.sage)
#
# class Test:
#     number=10
#     name="palle tech"
#     def __init__(self):
#         self.name="nitish"
#         print(self.name)
#         print(Test.name)
#         print(self.number)
# s1=Test()
# class Test:
#     number=10
#     name="palle tech"
#     def __init__(self):
#         self.name="nitish"
# t1=Test()
# print(t1.name)
# print(Test.name)
# print(t1.number)
# class Test:
#     x=10
#     y=20
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     @classmethod
#     def m1(cls):
#         print(cls.x)
#         print(cls.y)
#     def m2(self):
#         print(self.a)
#         print(self.b)
#     @staticmethod
#     def m3():
#         print("static method")
# s=Test(100,200)
# s.m2()
# Test.m1()
# Test.m3()
# class A:
#     def read(self):
#         print("student reading")
# class B(A):
#     def write(self):
#         print("student writing")
# d=B()
# d.read()
# d.write()
# class A:
#     x=10
#     def m1(self):
#         print("hello")
# class B(A):
#     y=20
#     def m2(self):
#         print(A.x)
# class C(B):
#     def m3(self):
#         print(A.x+B.y)
# c1=C()
# c1.m3()
# c1.m2()
# c1.m1()
# hirarchical inheritance
# class A:
#     x=10
#     def parent_class(self):
#         print("hello world")
# class B(A):
#     y=20
#     def g_class(self):
#         print(A.x+B.y)
# class C(A):
#     z=100
#     def s_class(self):
#         print(A.x+C.z)
# t1=C()
# t1.s_class()
# t1.g_class()
# t1.parent_class()
# class P1:
#     def m1(self):
#         print("original")
# class P2:
#     def m1(self):
#         print("duplicate")
# class C(P1,P2):
#     def m2(self):
#         print("original child")
# c1=C()
# c1.m1()
# c1.m2()
# class P:
#     def property(self):
#         print("gold")
#     def merry(self):
#         print("krishna")
# class C(P):
#     def merry(self):
#         print("manju")
#         super().merry()
# c1=C()
# c1.property()
# c1.merry()
# class P:
#     def __init__(self):
#         print("parent constructor")
# class C(P):
#     def __init__(self):
#         print("child constructor")
# c=C()
# class Persion:
#     def __init__(self, name, age):
#         self.name = name
#         self .age = age
# class Emp(Persion):
#     def __init__(self, name, age, eno, esal):
#         super().__init__(name, age)
#         self.eno=eno
#         self.esal=esal
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.eno)
#         print(self.esal)
# e1=Emp("mukul",23,66,589000)
# e1.display()
# class Poly:
#     def fun(self, x):
#         print(print(type(x)))
# s1=Poly()
# s1.fun(10)
# s1.fun("palle")
# def outer(fun):
#     def inner(x,y):
#         p=fun(x,y)
#         s=p[0]+' '+p[1]
#         s= s.upper()
#         d=s.split('')
#         return d
#     return inner
# @outer
# def m1(a,b):
#     return a,b
# z=m1("hello manju")
# print(z)
# def outer(fun):
#     def inner(p,q):
#         s=fun(p,q)
#         t=s[0]-s[1]
#         return t
#     return inner
# @outer
# def add(x,y):
#     return x,y
# a=add(10,20)
# print(a)
# import re
# x=input("enter the number")
# y=re.fullmatch('^\w+@\w+\.\w+$',x)
# s=re.fullmatch('[a-zA-Z]+\d+@gmail.com',x)
# p=re.fullmatch('\w+@gmail.com',x)
# print(x)
















