arr = [1, 2, 3, 4, 6]
target = 6

left, right = 0, len(arr) - 1

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print("Pair:", arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1