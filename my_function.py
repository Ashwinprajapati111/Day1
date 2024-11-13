# def birthday(name, age):
#     print (f"today is {name}'s birthday")
#     print (f"{name} is {age} years old")   
# birthday("ashwin", 36)
# birthday("sandip", 38)
# name = []
# age = []
# def enter():
#    b = input("Enter Your name: ")
#    c = input("Enter Your age: ")
#    name.append(b)
#    age.append(c)
#    return b,c   
# enter()
# enter()
# def entername_age(a,b):
#    ad = 0
#    while ad < len(a):
#       print(f"thank you {a[ad]}. You are {b[ad]} year old")
#       ad += 1   
# entername_age(name,age)
ourNum = int(input("Enter the number: "))   
def table(a,b):
   ourRange = range(1,11)
   for x in ourRange:
      result = b * x
      print(b," * ",x," = ",result)
      
table(5,ourNum)