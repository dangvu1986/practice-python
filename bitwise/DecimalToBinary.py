def decimal_to_binary(n):
    count = 0
    arr = []
    while n > 0:
        arr.append(n%2)
        count+=1
        n >>= 1
    str1 = "".join(str(i) for i in reversed(arr))
    print(str1)
    return count

print(decimal_to_binary(125))