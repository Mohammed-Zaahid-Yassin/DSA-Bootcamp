#Finding average of numbers in a list
def avg_list(avnum):
    if len(avnum) == 0:
        print("average = 0")
    else:
        k=sum(avnum) / len(avnum)
        print("average =",k)
n=int(input("Enter number of elements: "))
num_list=[]
for i in range(0,n):
    a=int(input("Enter element: "))
    num_list.append(a)
avg_list (num_list)