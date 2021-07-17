def is_multiple(n,m):
    return n%m == 0

def is_even(k):
    return k%2==0

def minmax(data):
    min, max = data[0], data[0]
    for i in range(1, len(data)):
        if min > data[i]:
            min = data[i]
        if max < data[i]:
            max = data[i]
    return min, max

'''min, max = minmax([1,2,3,4,5,6,7])
assert min == 1
assert max== 7
print("{0}, {1}".format(min, max)) '''


def get_sum_square(n):
    return sum([k*k for k in range(n)])

'''s = get_sum_square(3)
assert s == 5
print(s)'''


def get_sum_squares_odd(n):
    return sum([k*k for k in range(n) if k%2!=0])

from random import randrange

def get_random(data):
    index = randrange(len(data)-1)
    return data[index]


def scale(data, factor):
   for j in range(len(data)):
       data[j] *= factor

    
def dot_product(a, b):
    return [ia*ib for ia,ib in zip(a,b)]
