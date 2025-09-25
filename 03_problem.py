# A spam comment is defined as a text containing following keywords:
# "Make a lot of money”, "buy now”, "subscribe this”, "click this". Write a program to detect these spams.

message = input("enter your message : ")

if( ("Make a lot of money" in message) or ("buy now" in message) or ("subscribe this" in message)  or ("click this" in message) ):
    print("this message is spam")

else:
    print("this message is not spam")