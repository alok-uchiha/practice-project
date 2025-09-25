# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
#  Assume 3 subjects and take marks as an input from the user.


s1 = int(input("enter marks in frist subject : "))
s2 = int(input("enter marks in frist subject : "))
s3 = int(input("enter marks in frist subject : "))

# calculate the percentage


percentage = ((s1 + s2 + s3)/300)*100

if(percentage>=40 and s1>=33 and s2>=33 and s3>=33):
    print("your are passed : ",percentage)

else:
    print("your failed, try next year : ", percentage )