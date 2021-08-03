def find_max_sum_subArray_size_k(K, arr):
    max, sumArr, idxStart = 0, 0, 0

    for idxEnd in range(len(arr)):
        sumArr += arr[idxEnd]
        if idxEnd >= K-1:
            if sumArr > max:
                max = sumArr
            sumArr -= arr[idxStart]
            idxStart += 1
    return max

result = find_max_sum_subArray_size_k(3, [2, 1, 5, 1, 3, 2])
print("Max: " + str(result))