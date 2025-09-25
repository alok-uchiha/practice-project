# this program will give the greatest no entered


a = int(input("enter number"))
b = int(input("enter number"))
c = int(input("enter number"))
d = int(input("enter number"))


if(a>b and a>c and a>d):
    print("a is the greatest number", a)

elif(b>a and b>c and b>d):
    print("b is the greatest number", b) 

elif(c>a and c>b and c>d):
    print("c is the greatest number", c) 

elif(d>a and d>c and d>b):
    print("d is the greatest number", d)   