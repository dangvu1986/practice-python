def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        while i > 0 and arr[i-1] > current :
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = current

arr = [4,3, 1, 8, 9]

insertion_sort(arr)

print(arr)