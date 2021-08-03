def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

def merge(left, right, arr):
    i= j=k = 0
    lenL = len(left)
    lenR = len(right)

    while i < lenL and j < lenR :
        if left[i]<right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    while i < lenL:
        arr[k] = left[i]
        i+=1
        k+=1

    while j< lenR:
        arr[k] = right[j]
        j+=1
        k+=1


arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)