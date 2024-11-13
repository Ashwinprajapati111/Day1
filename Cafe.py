"""
piza = "Piza pirce is 98 Rs, "
sandwich = "sandwich price is 50 Rs, and "
burger = "burger price is 30 Rs"

pizaprice = 98
sandwichprice = 50  
burgerprice = 30
print(piza ,sandwich , burger)
order1 = input("enter your 1st order : ")
order2 = input("enter your 2nd order : ")
order3 = input("enter your 3rd order : ")
totalprice = []
print(order1, order2, order3)

if order1 == "piza" : 
    totalprice.append(pizaprice)
elif order1 == "sandwich":
    totalprice.append(sandwichprice)
elif order1 == "burger":
    totalprice.append(burgerprice)


if order2 == "piza" : 
    totalprice.append(pizaprice)
elif order2 == "sandwich":
    totalprice.append(sandwichprice)
elif order2 == "burger":
    totalprice.append(burgerprice)


if order3 == "piza" : 
    totalprice.append(pizaprice)
elif order3 == "sandwich":
    totalprice.append(sandwichprice)
elif order3 == "burger":
    totalprice.append(burgerprice)
print(totalprice)
tt = sum(totalprice)

print("your cost for all order is" , (sum(totalprice)))
"""


piza = "Piza pirce is 98 Rs, "
sandwich = "sandwich price is 50 Rs, and "
burger = "burger price is 30 Rs"

pizaprice = 98
sandwichprice = 50  
burgerprice = 30
print(piza ,sandwich , burger)
totalprice = []
order1 = input("enter your 1st order : ")
if order1 == "piza" : 
    totalprice.append(pizaprice)
elif order1 == "sandwich":
    totalprice.append(sandwichprice)
elif order1 == "burger":
    totalprice.append(burgerprice)

ask2 = input("do you want 2 order: ")
if ask2 == "yes":
    order2 = input("enter your 2nd order : ")
    if order2 == "piza":
        totalprice.append(pizaprice)       
    elif order2 == "sandwich":
        totalprice.append(sandwichprice)
    elif order2 == "burger":
        totalprice.append(burgerprice)      
else :
    print("your cost for all order is: " , (sum(totalprice)))

ask3 = input("do you want 3 order: ")
if ask3 == "yes":
    order3 = input("enter your 3rd order : ")
    if order3 == "piza":
        totalprice.append(pizaprice)       
    elif order3 == "sandwich":
        totalprice.append(sandwichprice)
    elif order3 == "burger":
        totalprice.append(burgerprice)  
    else :
        print("your cost for all order is: " , (sum(totalprice)))    
else :
    print("your cost for all order is: " , (sum(totalprice)))
print(totalprice)
print("your cost for today is: " , (sum(totalprice)))




