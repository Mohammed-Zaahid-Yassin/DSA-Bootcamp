#Two Sum
def two_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return [target - num, num]
        seen.add(num)
    return []


arr = [2, 7, 11, 15]
target = 13
result = two_sum(arr, target)
print(result)