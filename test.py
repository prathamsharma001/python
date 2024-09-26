# -># is used to comment the line
# -> it is also used to define the code meaning
# -> it can aslo comment and uncomment multiple lines using ctrl+ /

# comments example
# write a program to print your name
print("my name is pratham sharma")#print function to display statement

#variables can store the value and it can change at any time 
name = "pratham sharma"
#pass the variable in th eprint function
print("my name is"  + name) # + is used to concentrate the strings

#declare and initialize the multiple variables
age = 33
gender = "male"
email ="pratham05.ps@gmail.com"
#pass the multiple variable in print function 
# this line give the type error
#reason for error str can't be concentrate with integer
#prblem
# print("My name is"+ name +
#       "my age is "+ age + "and gender is "+ gender)
#solution 1 - int variable + replace by ,
"""
print("My name is "+ name+
      " my age is ", age," and gender is "+ gender)
#solution 2- enclosed the variable inside the string statement using f
# pass the variable in{}
print(f"My name is {name} my age is {age} my gender is {gender}my email is {email}")

#solution 3- using typecasting
ageinstring=str(age)
print("my name is "+ name+
      "my age is "+ ageinstring +"and gender is "+ gender)

#Data type in python 
print(type(name))# type function return datatype of variable 
print(type(age))
#1. str -> it can store the string data  e.g.name= "pratham sharma "
#2. int -> it can store the numeric data e.g.age=33
#3. float -> it can store the decimal no e.g. percentage =77.34

#typecasting in python:- convert one datatype to another datatypes
#e.g. sometime when we purchase item in float we paid in integer
purchaseitemprice= 33.22
paiditemprice= int(purchaseitemprice)
print("paid amount is", paiditemprice)

#Note ->string can't be converted into int reason string not ascii

#to get the input from user using input() function
collegename=input("enter your college name")
collegefee= int(input("enter your college fee"))
print("my college name is "+ collegename , collegefee)
# note:- the input function has default return type str
#add scholarship of 30000 in fee
collegefee=collegefee- 25000
print("after scholarship my fee", collegefee)
"""

# find the age in year when bornyear and currentyear given by user
currentyear=int(input("enter your currentyear"))
bornyear=int(input("enter your bornyear"))
age= currentyear-bornyear
print("your age is :",age)
                
dollar= int(input("enter no. in dollars"))
rupee=84 * dollar
print("no. in rupee", rupee)
