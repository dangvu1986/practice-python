def count_bit(x):
    rs = 0
    while x:
        print(x)
        print(x&1)
        rs += x&1
        x >>=1
    return rs

print(count_bit(12))