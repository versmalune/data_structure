#recursive
def factorial1(n):
    if (n == 0):
        return 1
    else:
        return n * factorial1(n - 1)
# time complexity: big o(n)



#iterative
def factorial2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# time complexity: big o(n)

# similar time when Big O notation is the same

print(factorial2(5))
print(factorial1(5))
