arr = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = current = arr[0]

for num in arr[1:]:
    current = max(num, current + num)
    max_sum = max(max_sum, current)

print("Max Sum:", max_sum)