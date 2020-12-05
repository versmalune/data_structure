def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



for i in range(11):
    print("f(%d) = %d" % (i, fibonacci(i)))

""" 수행 예: 
f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 2
f(4) = 3
f(5) = 5
f(6) = 8
f(7) = 13
f(8) = 21
f(9) = 34
f(10) = 55
"""