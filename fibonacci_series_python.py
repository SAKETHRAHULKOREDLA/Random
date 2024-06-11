def fibonacci_series(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_series(n-1)+fibonacci_series(n-2)

for i in range(10):
    print(fibonacci_series(i))