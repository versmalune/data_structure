#recursive
def power1(x, n):
    if (n == 0):
        return 1
    return x * power1(x, n - 1)
# time complexity : Big O(n)



#iterative
def power2(x, n):
    sum = 1
    for i in range(n):
        sum = sum * x
    return sum
# time complexity: Big O(n)



def power3(x, n):
    if (n == 0):
        return 1
    elif (n % 2 == 0):
        t = power3(x, n / 2)
        return t * t
    else:
        return x * power3(x, n - 1)
    return x * power3(x, x**n)



print(power1(2, 10))
print(power2(2, 10))
print(power3(2, 10))