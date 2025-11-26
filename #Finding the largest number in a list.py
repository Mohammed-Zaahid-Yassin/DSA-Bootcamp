#Finding the largest number in a list
numbers = []
print ("Enter the number of elements you want to add:")
n = int(input())
for i in range(n):
    print("Enter number", i + 1, ":")
    num = int(input())
    numbers.append(num)
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("The largest number is:", largest)