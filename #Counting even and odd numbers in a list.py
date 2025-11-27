#Counting even and odd numbers in a list
numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input("Enter number {}: "(i+1)))
    numbers.append(num)
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
