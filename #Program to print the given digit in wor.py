#Program to print the given digit in words
num =[]
n = int(input("Enter a number: "))
while n>0:
    r = n%10
    n = n//10
    num.append(r)
for r in reversed(num):
    match r:
        case 0: print("Zero", end=" ")
        case 1: print("One", end=" ")
        case 2: print("Two", end=" ")
        case 3: print("Three",end=" ")
        case 4: print("Four",end=" ")
        case 5: print("Five",end=" ")
        case 6: print("Six",end=" ")
        case 7: print("Seven",end=" ")
        case 8: print("Eight",end=" ")
        case 9: print("Nine", end=" ")
    
