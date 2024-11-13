# x = 100
# while x >= 1:
#     print(x)
#     x -= 1
# n = int(input("enter number"))
# i = 1
# while i <= 10 :
#     print (n*i)
#     i += 1

# name = ["hari", "krushna", "harikrishna"]
# idx = 0
# while idx < len(name):
#     print(name[idx])
#     idx += 1

# a = []
# ab1 = input("enter your 1 age: ")
# ab2 = input("enter your 2 age: ")
# ab3 = input("enter your 3 age: ")

# newlist=[ab1,ab2,ab3]
# a.extend(newlist)
# print(a)
# maxx = max(a)
# minn = min(a)
# print(maxx)
# print(minn)
mlist2 = ["hari","swami","narayan","fdasf"]
mlist = ["hari","swami","narayan"]

def lenn(a):
    print(len(a))
    return len(a)

def sameline(a):
    for b in a:
        print (b)
        
def cal_fact (a):
    d = 1
    for i in range (1, a+1):
        d *= i
        print(d)

def dol(usd_val):
    b = usd_val * 84
    print(usd_val, "USD = " , b , "INR")
dol(3)

