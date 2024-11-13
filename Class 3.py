#fname = input("enter your last name: ")
#lname = input("enter your email name: ")
#mpass = input("enter your password: ")
#cpass = input("enter your Confirm password: ")
#all = (fname , lname, mpass, cpass)
#print (all)
#print (len(all))
# Fname = input ("enter your name: ")
# Mpass = input("enter Password: ")
# Cpass = input("Enter Confirm Password: ")

# if Mpass == Cpass :
#     print ("welcome " + Fname + " to Shree Vachanamrut")

# else : print (Fname + "! your Password does not match")

# lengthf = (len(Fname))
# lengthm = (len(Mpass))
# print (len(Fname))
# print("My name length is : " , lengthf , "And My Password Lenght is : " , lengthm)
# print(Fname.count("a"))

# Marks = int(input("Enter Your Marks: "))
# if Marks >= 90 :
#     print("your grade is 'A'")
# elif Marks >= 80 and Marks <90 :
#     print("your grade is 'B'")
# elif Marks >= 70 and Marks <80 :
#     print("your grade is 'C'")
# elif Marks >= 60 and Marks <70 :
#     print("your grade is 'D'")
# else : print ("you are not qualified")

# Marks = int(input("Enter Your Marks: "))
# if Marks >= 90 :
#     grade = "A"
# elif Marks >= 80 and Marks <90 :
#     grade = "B"
# elif Marks >= 70 and Marks <80 :
#     grade = "C"
# elif Marks >= 60 and Marks <70 :
#     grade = "D"
# else : 
#     grade = "E"
# print(grade)


# Mnum = input("Enter A Number : ")
# if Mnum.endswith("2" or "4" or "6" or "8" or "0") :
#     print("this number is Odd")
# elif Mnum.endswith("1" or "3" or "5" or "7" or "9") :
#     print("this number is even")

# Mnum = int(input("Enter A Number : "))
# if Mnum % 2 == 0 :
#     print ("Odd")
# else :
#     print ("Even")

# f1= int(input("Enter First Number : "))
# f2= int(input("Enter Second Number : "))
# f3= int(input("Enter Third Number : "))

# if f1 > f2 and f1 > f3 :
#     print ("first is gretest number" , f1)
# elif f2 > f1 and f2 > f3 :
#     print ("Second is gretest number", f2)
# else :
#     print ("third is greatest number") 

# email = input("Enter your email: ")
# if email.endswith("@gmail.com"):
#     print("this is email")
# else :
#     print("this is not email")

# email1 = input("Enter your email: ")
# email2 = input("Enter your email: ")
# email3 = input("Enter your email: ")
# all=   (email1,email2,email3)
# print(len(all[1]))


# email1 = input("Enter your email: ")
# email2 = input("Enter your email: ")
# email3 = input("Enter your email: ")
# all=   (email1,email2,email3)

# if "hari" in all :
#     print ("you are in")
# else : 
#     print ("you are out")

# email1 = input("Enter your email: ")
# email2 = input("Enter your email: ")
# email3 = input("Enter your email: ")
# all=   (email1,email2,email3)
# hariindex = all.index("hari")
# print (hariindex)
# print (all)
# y = list(all)
# y[hariindex] = "swami"
# all = tuple(y)
# aappend = input("enter name to add: ")
# print(aappend)
# print(y)
# print(y.append(aappend))
# print(y)
# print(len(y))


list = ["a", "b" , "a", "c"]
tofind = (input("enter grade to fint: "))
countlist = list.count(tofind)

print(countlist)