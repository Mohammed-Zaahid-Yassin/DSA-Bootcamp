#Fibonacci series
n = int(input("Enter the number of Fibonacci terms to generate: "))
print(fibonacci(n))

def fibonacci(n):
    series = []
    a, b = 0, 1
    for x in range(n):
        series.append(a)
        a, b = b, a + b
    return series



