#l = [10,20,30,40,50]
#x=len(l)
# temp= l[0]
# l[0]=l[x-1]
# l[x-1]=temp
# print(l[0])
# print(l[x-1])
##################
# temp= l[0]
# l[0]=l[3]
# l[3]=temp
# print(l[0])
# print(l[3])
# #############
# string= "amaama"
# half=int(len(string)/2)
# x=string[:half]
# y=string[half:]
# if x==y:
#     print(string,"it is symmetric")
# else:
#     print(string,"it is not symmetric")
#
# #print("it is palendrome"if string==reversed(string) else "it is not palendrom")
# print("it is palendrome"if string==string[::-1] else "it is not palendrom")
#########################
# x="baab"
# y=x[::-1]
# if x==y:
#     print(x,"it is symmetic")
# else:
#     print(x,"it is not symmetric")
#
# print("it is palendrom" if x==y else "it is not palendrom")

# import re
# x='alrrla'
# if re.match("^(\w+)\Z",x) and x==x[::-1]:
#     print("palendrom")
# else:
#     print("not palendrom")
#
# import re
#
# x = "mukul nandi hii good"
# x = re.sub('\s+' , '', x)
# print(x)
########################
# n = int(input("enter the number"))
# s=0
# temp=n
# while(n>0):
#     p = n%10
#     s = s+(p**3)
#     n = n//10
# if temp==s:
#     print("it is a amstrong number")
# else:
#     print("it is not a amstrong number")
###############################
# start = int(input("enter the 1st number"))
# end = int(input("enter the 2nd number"))
# for n in range(start,end+1):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                break
#         else:
#             print(n)
####################################
# lower_value = int(input("Please, Enter the Lowest Range Value: "))
# upper_value = int(input("Please, Enter the Upper Range Value: "))
#
# print("The Prime Numbers in the range are: ")
# for number in range(lower_value, upper_value + 1):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)
###########################
# a,b=0,1
# for i in range(10):
#     print(a)
#     a,b = b ,a+b
#

###################
# n=int(input("enter the number"))
# fn=0
# sn=1
# print(fn)
# print(sn)
# for i in range(2,n):
#     tn=fn+sn
#     print(tn)
#     fn=sn
#     sn=tn
#     if tn==n:
#         print(n,"it is a fiboo")
#         break
# else:
#     print(n,"it is not fibbo")

########################
# def outer(fun):
#     def m2(x,y):
#         p=fun(x,y)
#         t=p[0]+p[1]
#         return t
#     return m2
#
# @outer
# def m3(a,b):
#     return a,b
# l=m3(12,13)
# print(l)
##################
# l=[1,5,3,4,2]
# l.sort(reverse=True)
# print(l)
################
# def bubble_sort_descending(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# l = [2, 1, 5, 4, 7, 6, 3]
# bubble_sort_descending(l)
# print("Sorted list in descending order:", l)
########################
# n = input("enter the element")
# ascii_value= ord(n)
# print(f"the ascii value of'{n}' is {ascii_value}")
####################
# Python Program for Sum of squares of first n natural numbers.
# n= int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     sum+=i**2
#     # sqr=sum**2
#     print(sum)
###########################
# n= int(input("enter the number"))
# cube=0
# for i in range(1,n+1):
#     cube+=i**3
#     print(cube)
############################
# Python Program to find sum of array
# l =[1,2,3,4,5,6]
# sum=0
# for i in l:
#     sum+=i
#     print(sum)
#################################
#Python Program to find largest element in an array
# l = [1, 2, 3, 4, 5, 6]
# big = l[0]
# for i in l:
#     if i>big:
#         big=i
# print(big)
#Python Program for array rotation
# import math
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*\
#             math.cos(2*k)-2*\
#             math.cos(3*k)-\
#             math.cos(4*k)
# speed(1000)
# bgcolor("black")
# for i in range(6000):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(5):
#         color("#f73487")
#     goto(0,0)
# done()
##############################
# l = [1, 3, 2, 6, 4, 5]
# big = l[0]
# for i in l:
#     if i>big:
#         big=i
# print(big)
# print(l[-2])
# print(l[1])
#################
# l = [2, 1, 4, 3, 6, 5]
# l.sort(reverse=True)
# print(l)
# print(f"the second biggest is {l[1]}")
# print(f"the second smallest is {l[-2]}")
###############################
# l = [2, 1, 4, 3, 6, 5]
# big=l[0]
# for i in l:
#     if i > big:
#         big = i
# print(big)
###############################

# l = [2, 1, 4, 3, 6, 5]
# # Initialize variables to store the smallest and second smallest elements
# smallest = float('inf')  # Initialize to positive infinity
# second_smallest = float('inf')  # Initialize to positive infinity

# Iterate through the list
# for num in l:
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num
#
# # Check if a second smallest element was found
# if second_smallest == float('inf'):
#     print("There is no second smallest element.")
# else:
#     print(f"The second smallest element is {second_smallest}")
######################----------------------------------------------------------#########################
# def rotateArray(a,d):
#     n=len(a)
#     a[:]=a[d:n]+a[0:d]
#     return a
#
# arr = [1, 2, 3, 4, 5, 6]
#
# print("Rotated list is")
# print(rotateArray(arr,2))
# #######################
# def m1(a,b):
#     n=len(a)
#     a[:]=a[b:n]+a[0:b]
#     return a
# arr=[1, 2, 3, 4, 5, 6]
# print("roted list")
# print(m1(arr,2))

###########################
# def rotate_array(arr, d):
#     n = len(arr)
#     d = d % n
#     arr[:] = arr[-d:] + arr[:-d]
#
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# d = 2
# rotate_array(arr, d)
# print("Rotated array:", arr)
###########################

#
# x=[1,1,2,5,18,15,14,18]
# y=max(x)
# z=[]
# for a in x:
#     if a!=y:
#         z.append(a)
# print(max(z))
#####################

# x = [1,1,2,5,18,15,14,18]
# y = set(x)
# x = list(y)
# x.remove(max(x))
# x.remove(min(x))
# print(max(x),min(x))
#####################
# Python program to split array and move first
# part to end.

# arr = [12, 10, 5, 6, 52, 36]
# n = len(arr)
# position = 2
# x = arr[:position]
# y = arr[position:]
# y.extend(x)
# for i in y:
# 	print(i, end=" ")
##########################################
# def m2(a,d):
#     n = len(a)
#     a[:]=a[d:n]+a[0:d]
#     return a
# arr=[12,10,5,6,52,36]
# print("the rotational array is")
# print(m2(arr,2))
#######################
# def isMonotonic(A):
#     return (all(A[i]<=A[i+1] for i in range(len(A)-1))or
#     all(A[i]>=A[i+1] for i in range(len(A)-1)))
# A=[1,2,3,4,5,6]
# print(isMonotonic(A))
#####################
#Python program to interchange first and last elements in a list
# def interchange(x):
#     x[0] ,x[-1] =x[-1] ,x[0]
#     return x
# x=[12, 35, 9, 56, 24]
# print(interchange(x))
############################
#Python program to swap two elements in a list
#swap two elements in list

# Swap 2nd position function
# def swapList(sl,pos1,pos2):
#     # Swapping
#     temp = sl[pos1]
#     sl[pos1] = sl[pos2]
#     sl[pos2] = temp
#     return sl

# l = [10, 14, 5,7,8, 9, 56, 12]
# pos1= 2
# pos2= len(l)-1
# n = len(l)
# x = n//2
# print(x)
# print(l)
# print("Swapped list: ",swapList(l,pos1-1,pos2-1))
# for i in range(0, x):
#     l[i], l[n-1] = l[n-1], l[i]
#     n = n-1
# print(l)




#######################################################################################################

# if 'INFOSYS' not in i['company']:
#     print(i['name'])employees={
#     'emp1':{'name':'Nitish','salary':20000,'company':['TCS','INFOSYS','WIPRO'],'htown':'hyd'},
#     'emp2':{'name':'Soumhya','salary':29000,'company':['v2','Bia'],'htown':'BPD'},
#     'emp3':{'name':'Raju','salary':2000,'company':['TCS','INFOSYS'],'htown':'JYP'},
#     'emp4':{'name':'Hari','salary':820000,'company':['k2','WIPRO'],'htown':'BBSR'},
#     'emp5':{'name':'Jadu','salary':30000,'company':['ABACUS','APMOSYS','WIPRO'],'htown':'CTC'},
#     'emp6':{'name':' Madhu','salary':20000,'company':['ABACUS','INFOSYS'],'htown':'BLS'},
# }
# sum = 0
# for i in employees.values():
#
#     sum = sum + i["salary"]
# print(sum)
#
#     # if 'INFOSYS' not in i['company']:
#     #     print(i['name'])



STR = "abcd"
substrings = []

for i in range(len(STR) - 1):
    substring = STR[i:i+2]
    substrings.append(substring)

print("All possible substrings of size two in '{}' are: {}".format(STR, substrings))







