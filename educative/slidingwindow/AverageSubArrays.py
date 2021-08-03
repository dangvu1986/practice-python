def find_averages_of_subarrays(K, arr):
    avgs = []
    sumArr = 0.0
    idxStart = 0

    for idxEnd in range(len(arr)):
        sumArr += arr[idxEnd]
        if idxEnd >= K-1:
            avgs.append(sumArr/K)
            sumArr -= arr[idxStart]
            idxStart += 1
    return avgs

result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))

