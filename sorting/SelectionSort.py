def selection_sort(arr):
    for i in range(len(arr)):
        s_idx = find_index_of_smallest_item(arr, i)
        arr[i], arr[s_idx] = arr[s_idx], arr[i]

def find_index_of_smallest_item(arr, start):
    s_idx = start
    for i in range(start, len(arr)):
        if (arr[s_idx] > arr[i]):
            s_idx = i
    return s_idx


arr = [7,5, 3, 8, 1, 2, 4]
selection_sort(arr)
print(arr)
