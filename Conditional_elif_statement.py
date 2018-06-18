print("begin")
x=input("Enter a positive no")
i=int(x)
if i<10:
    print("Given number is one digit no")
elif i<100:
    print("Given number is two Digit No")
elif i<1000:
    print("Given number is three digit number")
else:
    print("Given number is greater than the four digit nymber")
print("end")
