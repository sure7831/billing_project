item_1=500
item_2=2000

print("welcome_to_Billing_project")


print("item_1-price-500-----item_2-price-2000")

i=int(input("enter item number :"))

if i<=0:
        print("       ERROR       ")
        print("ITEM DOES NOT EXIST")
        print("program will continue with errors")
        print(" restart program to continue normally")
elif i>=3:

        print("       ERROR       ")
        print(" ITEM DOES NOT EXIST")
        print("program will continue with errors")
        print(" restart program to continue normally")



if i==1:

        i2=int(input("enter quantity"))
        cost=i2*500
elif i == 2 :

        i2=int(input("enter quantity"))

        cost=i2*2000
   


if 2 <= i2 <= 5:
    discount = 4 / 100
elif 1 <= i2 <= 2:
    discount = 10 / 100
elif 5 <= i2 <= 8:
    discount = 19 / 100
elif 11 <= i2 <= 40:
    discount = 24 / 100
elif i2 >= 12:
    discount = 29 / 100
else:
    discount =  2 / 100

SGST = 12 / 100
CGST = 12 / 100
product_SGST = cost * SGST
product_CGST = cost * CGST
product_discount =cost * discount
amount=int(input("enter amount to be paid"))
print("----------------------------------------------")
print("|               purchase again        |")
print("| total items purchased cost  :",cost,"  |")
print("| sgst                        :",SGST," |")
print("| cgst                        :",CGST," |")
print("| discount in  %              :",discount," |")
print("| amount to be paid            :",amount,"  |")
print("----------------------------------------------")