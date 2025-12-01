#Check if a number is divisible by 6
num= int(input("Enter the number:"))
if num % 6 ==0:
    a = int(num/6)
    print((num), "is divisible by 6 and ", a ," is the quotient.")
else:
    print((num), "is not divisible by 6")
