#factorial_of_a_number.py
n=input("Enter a number to find its factorial: ")
factorial=1
if int(n)<0:
    print("Factorial does not exist for negative numbers")
elif int(n)==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,int(n)+1):
        factorial=factorial*i
print("The factorial of",n,"is",factorial)
#End of the program