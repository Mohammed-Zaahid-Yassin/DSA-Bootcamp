#Finding the second largest number in a list
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest

first = second = 0
for number in numbers:
    if number > first:
        second = first
        first = number
    elif first > number > second:
        second = number
return second 