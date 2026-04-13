def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)

arr = [1, 2, 3, 4]
print("Sum of array:", sum_array(arr, len(arr)))