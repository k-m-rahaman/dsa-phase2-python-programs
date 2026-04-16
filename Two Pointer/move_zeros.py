arr = [0, 1, 0, 3, 12]

result = [x for x in arr if x != 0]
result += [0] * arr.count(0)

print(result)